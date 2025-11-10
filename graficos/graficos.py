import matplotlib.pyplot as plt
import pandas as pd


def crear_grafico(ingresos, egresos, ahorros):
    etiquetas = ["Ingresos", "Egresos", "Ahorros"]
    sizes = [ingresos, egresos, ahorros]
    explode = (0.1, 0.2, 0.1)
    colores = ["green", "red", "blue"]

    if ahorros > 0:

        fig, ax = plt.subplots()  # Creamos la figura y los ejes.
        ax.pie(
            sizes,
            explode=explode,
            labels=etiquetas,
            autopct="%1.1f%%",
            colors=colores,
            textprops={"color": "white"},
            shadow=True,
            startangle=90,
        )
        ax.axis("equal")
        fig.set_facecolor("#1C1C1E")
        return fig
    else:
        etiquetas = ["Ingresos", "Egresos"]
        sizes = [ingresos, egresos]
        explode = (0, 0.1)
        colores = ["green", "red"]
        fig, ax = plt.subplots()  # Creamos la figura y los ejes.
        fig.set_facecolor("#1C1C1E")
        ax.pie(
            sizes,
            explode=explode,
            labels=etiquetas,
            autopct="%1.1f%%",
            colors=colores,
            textprops={"color": "white"},
            shadow=True,
            startangle=90,
        )
        ax.axis("equal")
        return fig


def crear_grafico_tendencia(df_filtrado):
    """Esta función crea un gráfico de tendencias de ingresos y egresos"""

    if df_filtrado.empty:
        return None

    # Asegurarse que las columnas de las fechas sean datetime.
    df_filtrado = df_filtrado.copy()
    df_filtrado["fecha"] = pd.to_datetime(df_filtrado["fecha"])

    # Agrupar por categoría y fecha.
    df_agrupado = (
        df_filtrado.groupby(["fecha", "categoria"])["cantidad"].sum().reset_index()
    )

    # Separar ingresos y egresos
    ingresos_tiempo = df_agrupado[df_agrupado["categoria"] == "Ingresos"].copy()
    egresos_tiempo = df_agrupado[df_agrupado["categoria"] == "Egresos"].copy()

    # Si no hay gráficos para mostrar, retornar None.
    if ingresos_tiempo.empty and egresos_tiempo.empty:
        return None

    fig, ax = plt.subplots(figsize=(10, 5))
    fig.set_facecolor("#1C1C1E")
    ax.set_facecolor("#1C1C1E")

    # Graficar líneas
    if not ingresos_tiempo.empty:
        ax.plot(
            ingresos_tiempo["fecha"],
            ingresos_tiempo["cantidad"],
            marker="o",
            color="green",
            label="Ingresos",
            linewidth=2,
            markersize=6,
        )

    if not egresos_tiempo.empty:
        ax.plot(
            egresos_tiempo["fecha"],
            egresos_tiempo["cantidad"],
            marker="o",
            color="red",
            label="Egresos",
            linewidth=2,
            markersize=6,
        )

    ax.set_xlabel("Fecha", color="white", fontsize=10)
    ax.set_ylabel("Cantidad ($)", color="white", fontsize=10)
    ax.set_title(
        "Tendencia de Ingresos y Egresos", color="white", fontsize=14, fontweight="bold"
    )
    ax.tick_params(colors="white")
    ax.legend(facecolor="#2C2C2E", edgecolor="white", labelcolor="white")
    ax.grid(True, alpha=0.3, color="gray", linestyle="--")

    # Rotar etiquetas del eje x para mejor lectura.
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()

    return fig
