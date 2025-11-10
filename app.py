import streamlit as st
from main import CSV, crear_grafico, crear_grafico_tendencia
from data_entry import CATEGORIAS
from datetime import datetime
from chatbot_gemini import generar_respuesta_gemini
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from comandos import procesar_comando_rapido

# Constante para las variables de tiempo.
FORMAT = "%Y-%m-%d"

st.set_page_config(
    page_title="Finance Tracker",
    page_icon="💰",
    initial_sidebar_state="expanded",
)
st.title("📊 Agente de finanzas personales")
st.caption("Gestiona tus ingresos y egresos con ayuda de inteligencia artificial 💻 ")
eleccion = st.sidebar.radio(
    label="Menú ",
    options=[
        "🏠 Resumen financiero",
        "📪 Registrar transacción",
        "📅 Filtrar transacciones",
        "🗣️ Asistente Chatbot",
    ],
)
st.logo("logo.png", size="large")
if eleccion == "🏠 Resumen financiero":
    st.header("📈 Resumen Financiero")

    # Cargar todos los datos.
    try:
        df = pd.read_csv(CSV.CSV_FILE)
        df["fecha"] = pd.to_datetime(df["fecha"])

        # Calcular totales generales.
        total_ingresos = df[df["categoria"] == "Ingresos"]["cantidad"].sum()
        total_egresos = df[df["categoria"] == "Egresos"]["cantidad"].sum()
        balance_total = total_ingresos - total_egresos

        # Métricas principales.
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("💰 Ingresos totales", f"${total_ingresos:,.2f}")
        with col2:
            st.metric("💸 Egresos totales", f"${total_egresos:,.2f}")
        with col3:
            st.metric("📓 Balance total", f"${balance_total:,.2f}")

        # Crear el gráfico para los valores con plotly
        datos_year = ["Total ingresos", "Total egresos", "Balance total"]
        valores_year = [total_ingresos, total_egresos, balance_total]
        mapa = px.bar(
            x=datos_year,
            y=valores_year,
            color=valores_year,
            color_continuous_scale="Cividis",
            title=" 💵 Resumen gráfico",
        )
        st.plotly_chart(mapa)

        st.divider()

        # Resumen del mes actual.
        st.subheader("📆 Resumen del mes actual")
        mes_actual = datetime.now().month
        year_actual = datetime.now().year
        mask = (df["fecha"].dt.month == mes_actual) & (
            df["fecha"].dt.year == year_actual
        )
        df_mes = df[mask]

        if not df_mes.empty:
            ingresos_mes = df_mes[df_mes["categoria"] == "Ingresos"]["cantidad"].sum()
            egresos_mes = df_mes[df_mes["categoria"] == "Egresos"]["cantidad"].sum()
            total_mes = ingresos_mes - egresos_mes

            col1, col2, col3 = st.columns(3)
            col1.metric(f"Ingresos mes {mes_actual}", f"${ingresos_mes:,.2f}")
            col2.metric(f"Egresos mes {mes_actual}", f"${egresos_mes:,.2f}")
            col3.metric(f"Balance total mes  {mes_actual}", f"${total_mes:,.2f}")

            # Crear gráfico de los valores
            st.subheader(" 📊 Tendencias del mes")

            fig = go.Figure(
                data=[
                    go.Pie(
                        labels=["Ingresos", "Egresos"],
                        values=[ingresos_mes, egresos_mes],
                        hole=0.4,
                        marker_colors=["green", "red"],
                    )
                ]
            )

            fig.update_layout(
                title=f"Distribución - Mes {mes_actual}",
                template="plotly_dark",
                height=400,
            )
            st.plotly_chart(fig)

        else:
            st.info("No hay transacciones este mes.")

        st.divider()

        st.subheader("⏱️ Últimas transacciones")
        df_ordenado = df.sort_values("fecha", ascending=False).head(5)
        st.dataframe(df_ordenado, hide_index=True)

        # Número total de transacciones.
        st.caption(f"Total de transacciones registradas: {len(df)}")

    except FileNotFoundError:
        st.warning(
            "⚠️ ¡No hay datos todavía. ¡Comienza registrando tu primera transacción!"
        )
    except Exception as e:
        st.error(f"Error: {e}")

elif eleccion == "📪 Registrar transacción":
    st.header("📝 Registrar una nueva transacción")

    with st.form("transaction_form"):
        fecha = st.date_input("Fecha")
        cantidad = st.number_input("Cantidad", min_value=0.01, format="%.2f")
        categoria = st.selectbox("Categoria", options=list(CATEGORIAS.values()))
        descripcion = st.text_input(
            "Descripción", placeholder="Ej: Compra en supermercado"
        )

        enviar = st.form_submit_button("Guardar transacción")
        if enviar:
            CSV.agregar_entrada(
                fecha=fecha.strftime(FORMAT),
                cantidad=cantidad,
                categoria=categoria,
                descripcion=descripcion,
            )
            st.success("¡Transacción añadido con éxito!")
elif eleccion == "📅 Filtrar transacciones":
    st.header("💰 Resumen de transacciones")

    fecha_inicio = st.date_input("Fecha de inicio")
    fecha_final = st.date_input("Fecha final")

    if st.button("Ver resumen"):
        ingresos, egresos, ahorros, df_filtrado = CSV.filtrar_entrada(
            fecha_inicio=fecha_inicio.strftime(FORMAT),
            fecha_final=fecha_final.strftime(FORMAT),
        )

        if df_filtrado.empty:
            st.warning("No hay transacciones en el rango de fechas seleccionado.")
        else:
            st.write("Transacciones del período")
            st.dataframe(df_filtrado, hide_index=True)

            col1, col2, col3 = st.columns(3)
            col1.metric("Ingresos", f"${ingresos:,.2f}")
            col2.metric("Egresos", f"${egresos:,.2f}")
            col3.metric("Ahorros", f"${ahorros:,.2f}")

            # Mostrar el gráfico
            fig = crear_grafico(ingresos=ingresos, egresos=egresos, ahorros=ahorros)
            st.pyplot(fig=fig, width="stretch")

            st.divider()
            st.subheader("📈 Tendencia temporal")
            fig_tendencia = crear_grafico_tendencia(df_filtrado)
            if fig_tendencia:
                st.pyplot(fig=fig_tendencia)
            else:
                st.info("No hay suficientes datos para mostrar la tendencia.")

elif eleccion == "🗣️ Asistente Chatbot":
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
