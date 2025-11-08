import streamlit as st
from main import CSV, crear_grafico
from data_entry import CATEGORIAS
from datetime import datetime

FORMAT = "%Y-%m-%d"


st.title("📊 Agente de finanzas personales")
eleccion = st.sidebar.radio(
    label="Menú ", options=["Registrar transacción", "Ver Resumen Financiero"]
)

if eleccion == "Registrar transacción":
    st.header("📝 Registrar una nueva transacción")

    with st.form("transaction_form"):
        fecha = st.date_input("Fecha")
        cantidad = st.number_input("Cantidad", min_value=0.01, format="%.2f")
        categoria = st.selectbox("Categoria", options=list(CATEGORIAS.values()))
        descripcion = st.text_input("Descripción")

        enviar = st.form_submit_button("Guardar transacción")
        if enviar:
            CSV.agregar_entrada(
                fecha=fecha.strftime(FORMAT),
                cantidad=cantidad,
                categoria=categoria,
                descripcion=descripcion,
            )
            st.success("¡Transacción añadido con éxito!")
elif eleccion == "Ver Resumen Financiero":
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
            st.dataframe(df_filtrado)

            col1, col2, col3 = st.columns(3)
            col1.metric("Ingresos", f"${ingresos:,.2f}")
            col2.metric("Egresos", f"${egresos:,.2f}")
            col3.metric("Ahorros", f"${ahorros:,.2f}")

            # Mostrar el gráfico
            fig = crear_grafico(ingresos=ingresos, egresos=egresos, ahorros=ahorros)
            st.pyplot(fig=fig)
