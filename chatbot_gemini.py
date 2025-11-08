import streamlit as st
import google.generativeai as genai
import pandas as pd

# Configurar la clave API de Google.
genai.configure(api_key=st.secrets["GEMINI_API_KEY"])


def generar_respuesta_gemini(pregunta_usuario: str, datos_df: pd.DataFrame) -> str:
    # Convertir los datos del Dataframe en un formato que Gemini pueda entender.
    # Se usa markdown para que sea legible.
    datos_financieros_str = datos_df.to_markdown(index=False)

    # Contruir el prompt para Gemini
    prompt = f"""Eres un asistente financiero experto. Tu tarea es responder a las preguntas del usuario asándote únicamente en los datos financieros que te proporciono a continuación. Si la pregunta no puede ser respondida con los datos proporcionados, por favor, indica que no tienes suficiente información. 

    ---
    Datos Financieros:
    {datos_financieros_str}
    ---
    Pregunta del usuario:
    {pregunta_usuario}
    Tu respuesta:
    """

    # Inicializar el modelo de Gemini
    model = genai.GenerativeModel("gemini-2.5-pro")

    try:
        # Generar contenido con el modelo
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return "Lo siento, hubo un error en la solicitud {e}"
