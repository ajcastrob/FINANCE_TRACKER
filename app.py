import streamlit as st
from pages.load_csv import pag0
from pages.resumen import pag1
from pages.trasaccion import pag2
from pages.filtro import pag3
from pages.chat import pag4


st.set_page_config(
    page_title="Finance Tracker",
    page_icon="💰",
    layout="wide",
    initial_sidebar_state="expanded",
)
# Constantes.
IMAGEN_LOGO = "./assets/logo.png"
st.image(IMAGEN_LOGO, width=80)

st.logo(IMAGEN_LOGO, size="large")


st.title("📊 Agente de finanzas personales")
st.caption("Gestiona tus ingresos y egresos con ayuda de inteligencia artificial 💻 ")

st.sidebar.write("Páginas de contacto")

st.sidebar.page_link(
    "https://www.linkedin.com/in/josé-castro-b600791a4/",
    label="LinkedIn",
    icon="📩",
)
st.sidebar.page_link(
    "https://github.com/ajcastrob/finance_tracker?tab=readme-ov-file",
    label="Repositorio Github",
    icon="🛠️",
)

st.sidebar.divider()
st.sidebar.markdown(
    """
Hecho con ❤️ por José A. Castro 
"""
)


pg = st.navigation(
    {
        "Bienvenida": [st.Page(pag0, title="Subir CSV", icon="📓")],
        "Menú": [
            st.Page(pag1, title="Resumen financiero", icon="🧮"),
            st.Page(pag2, title="Registrar transacción", icon="📪"),
            st.Page(pag3, title="Filtrar transacción", icon="📅"),
        ],
        "Asistente financiero IA": [st.Page(pag4, title="AdamBot", icon="🗣️")],
    }
)
pg.run()
