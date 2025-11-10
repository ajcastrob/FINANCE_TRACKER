import streamlit as st
from csv_file import CSV
from chatbot.chatbot_gemini import generar_respuesta_gemini
from chatbot.comandos import procesar_comando_rapido
import pandas as pd


def pag4():
    st.header(" 💬 Tu IA Financiero")
    st.markdown(
        """
    <style>
        .stChatMessage {
            border-radius: 10px;
            padding: 10px;
            margin: 5px 0;
        }
    </style>
    """,
        unsafe_allow_html=True,
    )
    st.caption("Pregúntame sobre tus finanzas o usa comandos rápidos")

    with st.expander("💡 Comandos y Preguntas Sugeridas"):
        col1, col2 = st.columns(2)

        with col1:
            st.markdown("**⚡ Comandos Rápidos:**")
            st.code("/resumen -Resumen general")
            st.code("/mes - Resumen del mes")
            st.code("/semana - Últimos 7 días")
            st.code("/analisis - Análisis con IA")
            st.code("/ayuda - Mostrar ayuda")

        with col2:
            st.markdown("**💬 Preguntas Sugeridas:**")
            st.markdown(
                """
            - ¿Cuánto he gastado esta semana?
            - ¿Cuál es mi balance actual?
            - ¿En qué categoría gasto más?
            - Analiza mis gastos del último mes
            - ¿Tengo gastos altos recientes?

            """
            )

    # Inicializar el estado del chat si no existe
    if "messages" not in st.session_state:
        st.session_state.messages = []
        # Mensaje de bienvenida.
        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": "¡Hola! 👋 Soy tu asistente financiero personal. Puedo ayudarte a analizar tus finanzas, responder preguntas sobre tus gastos e ingresos, y darte recomendaciones. Usa `/ayuda` para ver los comandos disponibles o simplemente pregúntame lo que necesites.",
            }
        )

    # Mostrar mensajes previos del historial
    for message in st.session_state.messages:
        avatar = "🦾" if message["role"] == "assistant" else "🗣️"
        with st.chat_message(message["role"], avatar=avatar):
            st.markdown(message["content"])

    # Capturar la entrada del usuario.
    if prompt := st.chat_input(
        "Escribe tu pregunta o usa un comando (ej: /resumen)..."
    ):
        # Añadir el mensaje del usuario al historial
        st.session_state.messages.append(
            {
                "role": "user",
                "content": prompt,
            }
        )
        with st.chat_message("user", avatar="🗣️"):
            st.markdown(prompt)

        # Procesar la solicitud del usuario.
        with st.chat_message("assistant", avatar="🦾"):
            # Mostrar indicador de "escribiendo"
            with st.spinner("🧠Pensando..."):
                try:
                    # Cargar los datos financieros.
                    df_finanzas = pd.read_csv(CSV.CSV_FILE)

                    # Verificar si es un comando rápido
                    response = None
                    if prompt.startswith("/"):
                        response = procesar_comando_rapido(prompt, df_finanzas)

                    # Si no es un comando o el comando no fue reconocido, usar Gemini
                    if response is None:
                        response = generar_respuesta_gemini(
                            prompt,
                            df_finanzas,
                            historial_conversacion=st.session_state.messages[
                                :-1
                            ],  # Excluir el último mensaje
                        )

                    st.markdown(response)
                except FileNotFoundError:
                    response = "⚠️ No hay datos financieros disponibles todavía. Por favor, registra algunas transacciones primero."
                    st.markdown(response)
                except Exception as e:
                    response = f"❌ Lo siento, hubo un error: {str(e)}"
                    st.markdown(response)

        st.session_state.messages.append({"role": "assistant", "content": response})

    st.divider()
    col1, col2, col3 = st.columns([1, 1, 1])
    with col2:
        if st.button("🗑️ Limpiar conversación"):
            st.session_state.messages = []
            st.rerun()
