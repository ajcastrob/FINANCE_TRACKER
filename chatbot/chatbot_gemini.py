import streamlit as st
import google.generativeai as genai
import pandas as pd
from chatbot.contexto import obtener_contexto_financiero

# Configurar la clave API de Google.
genai.configure(api_key=st.secrets["GEMINI_API_KEY"])


# Función para llamar al modelo de Gemini
@st.cache_resource
def cargar_modelo_gemini():
    """Carga el módelo de gemini y aprovecha el cacheo para no gastar más llamadas"""
    return genai.GenerativeModel(
        "gemini-2.5-flash",
        generation_config={
            "temperature": 0.7,
        },
    )


def generar_respuesta_gemini(
    pregunta_usuario: str, datos_df: pd.DataFrame, historial_conversacion: list = None
) -> str:
    """Generar una respuesta con el módelo de Gemini"""
    try:
        # Obtener el contexto financiero del dataset
        contexto = obtener_contexto_financiero(datos_df)

        # Crear resumen de transacciones con formato limpio
        # Limitar a las últimas 100 transacciones para no sobrecargar el prompt
        if len(datos_df) > 100:
            datos_recientes = datos_df.tail(100)
            nota_transacciones = f"\n Mostrando 100 transacciones de {len(datos_df)} transacciones totales.\n"
        else:
            datos_recientes = datos_df
            nota_transacciones = ""

        # Formatear transacciones con saltos de línea explícitos.
        transacciones_texto = "TRANSACCIONES RECIENTES:" + nota_transacciones
        for idx, row in datos_recientes.iterrows():
            # formatear la fecha
            if pd.notna(row["fecha"]):
                fecha_str = pd.to_datetime(row["fecha"]).strftime("%Y-%m-%d")
            else:
                fecha_str = "N/A"

            # crear línea de transacción
            transacciones_texto += f"\n. {fecha_str} | $ {row["cantidad"]:,.2f} |  {row["categoria"]} | {row["descripcion"]}"

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

        # Cargar el módelo de Gemini llamando a la función
        model = cargar_modelo_gemini()

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
        return f"❌ Error al procesar pregunta: {str(e)}"
