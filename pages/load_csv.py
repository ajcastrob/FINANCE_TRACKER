import streamlit as st
import pandas as pd
from pathlib import Path

# Directorio a guardar CSV
DIRECTORIO = Path(__file__).parent.parent
IMAGE = "./assets/example.png"


def pag0():

    st.markdown(
        """### 💰 Tu asistente personal de finanzas

Gestiona tus ingresos y egresos de forma inteligente con visualizaciones interactivas y análisis conversacional con la ayuda de IA."""
    )

    st.divider()

    st.markdown(
        """Esta una aplicación moderna de gestión financiera personal que combina:

        - 📊 **Visualizaciones Interactivas** - Gráficos dinámicos con Plotly y Matplotlib
        - 🦾 **Chatbot con IA** - Análisis conversacional usando un asistente inteligente potenciado con Google Gemini
        - 📱 **Interfaz Moderna** - Diseño multi-página con Streamlit
        - 💾 **Gestión Simple** - Uso de formato CSV, fácil de usar
"""
    )

    with st.expander("💼 Características destacas"):
        st.markdown(
            """
        ### 🏠 Dashboard Financiero
        Visualiza tu situación financiera completa de un vistazo:
        - Balance total en tiempo real
        - Métricas del mes actual
        - Últimas 5 transacciones
        - Gráficos comparativos interactivos

        ### 💬 Chatbot Inteligente (AdamBot)
        Interactúa con tus finanzas en lenguaje natural:

        **Comandos Rápidos:**
        - `/resumen` → Vista general de tus finanzas
        - `/mes` → Análisis del mes actual
        - `/semana` → Últimos 7 días
        - `/analisis` → Insights con IA

        **Pregunta al asistente:**
        - "¿Cuál es mi balance actual?"
        - "¿Cuánto gasté la semana pasada?"
        - "¿En qué categoría gasto más?"

        ### 📈 Análisis Avanzados
        - Gráficos de tendencia temporal
        - Comparativas por categorías
        - Filtros por rangos de fechas
        - Detección de patrones de gastos
        """
        )

    st.divider()

    st.markdown("### 🚀 Inicio Rápido: Sube tu archivo de finanzas en formato CSV")
    st.write("El archivo csv debe seguir el siguiente módelo")
    st.image(image=IMAGE)

    try:
        file_csv = st.file_uploader("Subir", type=["csv"])

        if file_csv is not None:
            # Leer archivo con pandas
            if file_csv.name.endswith("csv"):
                df = pd.read_csv(file_csv)

        st.write("Archivo leído con éxito")

        # Renombrar el archivo para poder trabajar con la clase que se creó CSV.
        route = Path(file_csv.name)
        new_name = route.with_name("finanzas_personales.csv")

        destiny_route = DIRECTORIO.joinpath(new_name.name)

        # Guardar archivo en el directorio padre.
        df.to_csv(destiny_route, index=False)

        st.success("El archivo está registrado correctamente.")

    except UnboundLocalError:
        pass
    except AttributeError:
        pass
