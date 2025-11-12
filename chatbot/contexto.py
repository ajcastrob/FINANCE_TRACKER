import streamlit as st
import pandas as pd
from datetime import datetime, timedelta


def obtener_contexto_financiero(datos_df: pd.DataFrame) -> dict:
    """Extrae información clave de los datos financieros para proporcionar contexto al chatbot"""

    if datos_df.empty:
        return {"mensaje": "No hay datos financieros disponibles"}

    # Convertir la fecha a datetime si no lo es.
    datos_df["fecha"] = pd.to_datetime(datos_df["fecha"])

    # Calcular datos generales
    total_ingresos = datos_df[datos_df["categoria"] == "Ingresos"]["cantidad"].sum()
    total_egresos = datos_df[datos_df["categoria"] == "Egresos"]["cantidad"].sum()
    balance_total = total_ingresos - total_egresos

    # Datos del último mes
    ultimos_dias = datetime.now() - timedelta(days=30)
    df_mes = datos_df[datos_df["fecha"] >= ultimos_dias]
    ingresos_mes = df_mes[df_mes["categoria"] == "Ingresos"]["cantidad"].sum()
    egresos_mes = df_mes[df_mes["categoria"] == "Egresos"]["cantidad"].sum()

    # Última transacción
    ultima_transaccion = datos_df.sort_values("fecha", ascending=False).iloc[0]

    # Estadísticas adicionales.
    total_transacciones = len(datos_df)
    promedio_ingresos = datos_df[datos_df["categoria"] == "Ingresos"]["cantidad"].mean()
    promedio_egresos = datos_df[datos_df["categoria"] == "Egresos"]["cantidad"].mean()

    # Crear el diccionario con los datos que se le pasará a gemini
    contexto = {
        "total_ingresos": total_ingresos,
        "total_egresos": total_egresos,
        "balance_total": balance_total,
        "ingresos_ultimos_30_dias": ingresos_mes,
        "egresos_ultimos_30_dias": egresos_mes,
        "total_transacciones": total_transacciones,
        "promedio_ingresos": promedio_ingresos,
        "promedio_egresos": promedio_egresos,
        "ultima_fecha": ultima_transaccion["fecha"].strftime("%Y-%m-%d"),
        "ultima_cantidad": ultima_transaccion["cantidad"],
        "ultima_categoria": ultima_transaccion["categoria"],
    }

    # Devolver el diccionario
    return contexto
