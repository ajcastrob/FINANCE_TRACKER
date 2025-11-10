import google.generativeai as genai
import pandas as pd
from chatbot.contexto import obtener_contexto_financiero


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
