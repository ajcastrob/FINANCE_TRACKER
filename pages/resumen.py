import streamlit as st
from datetime import datetime
from csv_file import CSV
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go


def pag1():
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
