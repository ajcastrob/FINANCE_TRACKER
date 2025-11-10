import streamlit as st
from data_entry import CATEGORIAS
from csv_file import CSV

FORMAT = "%Y-%m-%d"


def pag2():
    st.header("📝 Registrar una nueva transacción")

    with st.form("transaction_form"):
        fecha = st.date_input("Fecha")
        cantidad = st.number_input("Cantidad", step=0.01, min_value=0.01, format="%.2f")
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
