import streamlit as st
from csv_file import CSV
from graficos.graficos import crear_grafico, crear_grafico_tendencia

FORMAT = "%Y-%m-%d"


def pag3():
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
