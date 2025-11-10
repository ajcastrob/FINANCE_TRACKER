import pandas as pd
from datetime import datetime, timedelta
from chatbot_analisis import analizar_finanzas_proactivo


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
