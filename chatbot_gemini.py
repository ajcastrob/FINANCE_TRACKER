import streamlit as st
import google.generativeai as genai
import pandas as pd
from datetime import datetime, timedelta

# Configurar la clave API de Google.
genai.configure(api_key=st.secrets["GEMINI_API_KEY"])


def obtener_contexto_financiero(datos_df: pd.DataFrame) -> dict:
    """Extrae información clave de los datos financieros para proporcionar contexto al chatbot"""

    if datos_df.empty:
        return {"mensaje": "No hay datos financieros disponibles"}

    # Convertir la fecha a datetime si no lo es.
    datos_df["fecha"] = pd.to_datetime(datos_df["fecha"])

    # Calcular datos generales
    total_ingresos = datos_df[datos_df["categoria"] == "Ingresos"]["cantidad"].sum()
    total_egresos = datos_df[datos_df["categoria"] == "Egresos"]["cantidad"].sum()
    balance_total = total_ingresos - total_egresos

    # Datos del último mes
    ultimos_dias = datetime.now() - timedelta(days=30)
    df_mes = datos_df[datos_df["fecha"] >= ultimos_dias]
    ingresos_mes = df_mes[df_mes["categoria"] == "Ingresos"]["cantidad"].sum()
    egresos_mes = df_mes[df_mes["categoria"] == "Egresos"]["cantidad"].sum()

    # Última transacción
    ultima_transaccion = datos_df.sort_values("fecha", ascending=False).iloc[0]

    # Estadísticas adicionales.
    total_transacciones = len(datos_df)
    promedio_ingresos = datos_df[datos_df["categoria"] == "Ingresos"]["cantidad"].mean()
    promedio_egresos = datos_df[datos_df["categoria"] == "Egresos"]["cantidad"].mean()

    # Crear el diccionario con los datos que se le pasará a gemini
    contexto = {
        "total_ingresos": total_ingresos,
        "total_egresos": total_egresos,
        "balance_total": balance_total,
        "ingresos_ultimos_30_dias": ingresos_mes,
        "egresos_ultimos_30_dias": egresos_mes,
        "total_transacciones": total_transacciones,
        "promedio_ingresos": promedio_ingresos,
        "promedio_egresos": promedio_egresos,
        "ultima_fecha": ultima_transaccion["fecha"].strftime("%Y-%m-%d"),
        "ultima_cantidad": ultima_transaccion["cantidad"],
        "ultima_categoria": ultima_transaccion["categoria"],
    }

    # Devolver el diccionario
    return contexto


def generar_respuesta_gemini(
    pregunta_usuario: str, datos_df: pd.DataFrame, historial_conversacion: list = None
) -> str:
    """Generar una respuesta con el módelo de Gemini"""
    try:
        # Obtener el contexto financiero del dataset
        contexto = obtener_contexto_financiero(datos_df)

        # Crear resumen de transacciones con formato limpio
        # Limitar a las últimas 50 transacciones para no sobrecargar el prompt
        if len(datos_df) > 500:
            datos_recientes = datos_df.tail(500)
            nota_transacciones = f"\n Mostrando las últimas 500 de {len(datos_df)} transacciones totales.\n"
        else:
            datos_recientes = datos_df
            nota_transacciones = ""

        # Formatear transacciones con saltos de línea explícitos.
        transacciones_texto = "TRANSACCIONES RECIENTES:" + nota_transacciones
        for idx, row in datos_recientes.iterrows():
            # formatear la fecha
            if pd.notna(row["fecha"]):
                fecha_str = pd.to_datetime(row["fecha"].strftime("%Y-%m-%d"))
            else:
                fecha_str = "N/A"

            # crear línea de transacción
            transacciones_texto += f"\n. {fecha_str} | {row["categoria"]} | $ {row["cantidad"]:,.2f} | {row["descripcion"]}"

        # Contruir el historial de conversación de Gemini
        historial_gemini = []
        if historial_conversacion:
            for msg in historial_conversacion[
                -4:
            ]:  # Solo los últimos cuatro para no exceder límites
                rol = "user" if msg["role"] == "user" else "model"
                historial_gemini.append({"role": rol, "parts": [msg["content"]]})

        # Prompt limpio con formato estructurado.
        prompt_sistema = f"""Eres AdamBot 💰, un asistente financiero profesional y amigable.
                RESUMEN FINANCIERO DEL USUARIO:
            ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
            - Balance Total: $ {contexto.get('balance_total', 0):,.2f}
            - Ingresos Totales: $ {contexto.get('total_ingresos', 0):,.2f}
            - Egresos Totales: $ {contexto.get('total_egresos', 0):,.2f}
            - Total de Transacciones: {contexto.get('total_transacciones', 0)}

                ÚLTIMOS 30 DÍAS:
            - Ingresos: $ {contexto.get('ingresos_ultimos_30_dias', 0):,.2f}
            - Egresos: $ {contexto.get('egresos_ultimos_30_dias', 0):,.2f}

            ÚLTIMA TRANSACCIÓN:
            - Categoría: {contexto.get('ultima_categoria', 'N/A')}
            - Monto: $ {contexto.get('ultima_cantidad', 0):,.2f}
            - Fecha: {contexto.get('ultima_fecha', 'N/A')}

            {transacciones_texto}

            ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
                    INSTRUCCIONES IMPORTANTES:
            1. Responde basándote ÚNICAMENTE en los datos proporcionados arriba
            2. Mantén tus respuestas concisas: máximo 100 palabras
            3. Usa espacios correctos entre TODAS las palabras y números
            4. Formatea cantidades monetarias como: "$ 1,234.56" (siempre con espacio después del $)
            5. Usa emojis con moderación para hacer la conversación amigable
            6. Si detectas patrones preocupantes, menciónalos con tacto
            7. Proporciona análisis numéricos cuando sea relevante

            PREGUNTA DEL USUARIO:
            {pregunta_usuario}
            TU RESPUESTA (recuerda: espacios claros entre palabras):"""

        model = genai.GenerativeModel(
            "gemini-2.5-flash",
            generation_config={
                "temperature": 0.7,
            },
        )

        # Crear una sesión con el historial del chat
        chat = model.start_chat(history=historial_gemini)

        # Generar una respuesta
        response = chat.send_message(prompt_sistema)

        # Verificar que la respuesta tenga contenido
        if response.parts:
            texto = response.text
            # Post-procesamiento para garantizar espacios correctos
            texto = texto.replace("$", "$ ")  # Eliminar espacios después de $
            texto = texto.replace("  ", " ")  # Eliminar espacios dobles
            texto = texto.strip()

            # Retornar la respuesta
            return texto
        else:
            return f"❌ No pude generar una respuesta."
    except Exception as e:
        return f"❌ Errar al procesar pregunta: {str(e)}"


def analizar_finanzas_proactivo(datos_df: pd.DataFrame) -> str:
    """
    Genera un análisis proactivo de las finanzas del usuario
    """
    if datos_df.empty:
        return "No hay suficientes datos para analizar"

    contexto = obtener_contexto_financiero(datos_df)

    prompt = f"""Como experto financiero, analiza estos datos y proporciona 3 insights claves:

    Balance total: ${contexto['balance_total']:,.2f}\n
    Ingresos totales: ${contexto['total_ingresos']:,.2f}\n
    Egresos totales: ${contexto['total_egresos']:,.2f}\n
    Últimos 30 días - Ingresos: ${contexto['ingresos_ultimos_30_dias']:,.2f}\n
    Últimos 30 días - Egresos: ${contexto['egresos_ultimos_30_dias']:,.2f}\n

    Proporciona:
    1. Una observación sobre la salud financiera
    2. Una tendencia que detectes
    3. Una recomendación práctica

    Sé breve (máximo 100 palabras). Usa espacios claros entre palabras y números. Y usa emojis."""

    model = genai.GenerativeModel("gemini-2.5-flash")

    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"No se pudo generar el análisis: {str(e)}"


def procesar_comando_rapido(comando: str, datos_df: pd.DataFrame) -> str:
    """
    Procesa comandos rápidos del usuario
    """

    comando = comando.lower().strip()

    if datos_df.empty:
        return "🪛 No hay datos disponibles para procesar comando."

    datos_df["fecha"] = pd.to_datetime(datos_df["fecha"])

    # Comando /resumen:

    if comando == "/resumen":
        total_ingresos = datos_df[datos_df["categoria"] == "Ingresos"]["cantidad"].sum()
        total_egresos = datos_df[datos_df["categoria"] == "Egresos"]["cantidad"].sum()
        balance = total_ingresos - total_egresos
        total_transacciones = len(datos_df)

        return f"""
        💰 Ingresos totales: ${total_ingresos:,.2f}\n
        💸 Egresos totales: ${total_egresos:,.2f}\n
        📈 Balance: ${balance:,.2f}\n
        📝 Total transacciones: {total_transacciones}
                """

    # Comando /mes:

    elif comando == "/mes":
        mes_actual = datetime.now().month
        year_actual = datetime.now().year
        mask = (datos_df["fecha"].dt.month == mes_actual) & (
            datos_df["fecha"].dt.year == year_actual
        )
        df_mes = datos_df[mask]

        if df_mes.empty:
            return "📭 No hay transacciones este mes."

        ingresos_mes = df_mes[df_mes["categoria"] == "Ingresos"]["cantidad"].sum()
        egresos_mes = df_mes[df_mes["categoria"] == "Egresos"]["cantidad"].sum()
        balance_mes = ingresos_mes - egresos_mes

        return f"""📅 **Resumen del Mes Actual ({mes_actual}/{year_actual})
        💰 Ingresos: ${ingresos_mes:,.2f}\n
        💸 Egresos: ${egresos_mes:,.2f}\n
        📈 Balance: ${balance_mes:,.2f}\n
        
        """

    # Comando /semana
    elif comando == "/semana":
        hace_7_dias = datetime.now() - timedelta(days=7)
        df_semana = datos_df[datos_df["fecha"] >= hace_7_dias]

        if df_semana.empty:
            return "📭 No hay transacciones en los últimos 7 días."

        ingresos = df_semana[df_semana["categoria"] == "Ingresos"]["cantidad"].sum()
        egresos = df_semana[df_semana["categoria"] == "Egresos"]["cantidad"].sum()
        balance = ingresos - egresos

        return f"""📆 **Últimos 7 Días**
        💰 Ingresos: ${ingresos:,.2f}\n
        💸 Egresos: ${egresos:,.2f}\n
        📈 Balance: ${balance:,.2f}\n
        """

    # Comando /ayuda
    elif comando == "/ayuda":
        return """🖥️ **Comandos Disponibles:**
        `/resumen` - Resumen general de todas tus finanzas
        `/mes` - Resumen del mes actual
        `/semana` - Resumen de los últimos 7 días
        `/analisis` - Análisis detallado con IA
        `/ayuda` - Muestra este mensaje

        También puedes hacer preguntas en lenguaje natural como:
        - "¿Cuánto gasté en la última semana?"
        - "¿Cuál es mi balance actual?"
        - "¿En qué he gastado más?"
        """
    # Comando análisis
    elif comando == "/analisis":
        return analizar_finanzas_proactivo(datos_df)

    else:
        return None  # No es un comando conocido
