import streamlit as st
from pages.resumen import pag1
from pages.trasaccion import pag2
from pages.filtro import pag3
from pages.chat import pag4


# Constantes.
FORMAT = "%Y-%m-%d"
IMAGEN_LOGO = "assets/logo.png"

st.set_page_config(
    page_title="Finance Tracker",
    page_icon="💰",
    initial_sidebar_state="expanded",
)
st.image(IMAGEN_LOGO, width=80)
st.logo(IMAGEN_LOGO, size="large")


st.title("📊 Agente de finanzas personales")
st.caption("Gestiona tus ingresos y egresos con ayuda de inteligencia artificial 💻 ")

st.sidebar.page_link(
    "https://www.linkedin.com/in/josé-castro-b600791a4/",
    label="LinkedIn",
    icon="📩",
)


pg = st.navigation(
    [
        st.Page(pag1, title="Resumen financiero", icon="🏠"),
        st.Page(pag2, title="Registrar transacción", icon="📪"),
        st.Page(pag3, title="Filtrar transacción", icon="📅"),
        st.Page(pag4, title="Asistente Chatbot", icon="🗣️"),
    ]
)
pg.run()
