import pandas as pd
import csv
from datetime import datetime
from data_entry import (
    obtener_cantidad,
    obtener_categoria,
    obtener_descripcion,
    obtener_fecha,
)
import matplotlib.pyplot as plt


class CSV:
    CSV_FILE = "finanzas_personales.csv"
    COLUMNS = ["fecha", "cantidad", "categoria", "descripcion"]
    FORMAT = "%Y-%m-%d"

    @classmethod
    def crear_csv_inicial(cls):
        try:
            df = pd.read_csv(cls.CSV_FILE)
        except FileNotFoundError:
            df = pd.DataFrame(columns=cls.COLUMNS)
            df.to_csv(cls.CSV_FILE, index=False)
            print("🗒️ Archivo creado con éxito.")

    @classmethod
    def agregar_entrada(cls, fecha, cantidad, categoria, descripcion):
        nueva_entrada = {
            "fecha": fecha,
            "cantidad": cantidad,
            "categoria": categoria,
            "descripcion": descripcion,
        }

        with open(cls.CSV_FILE, "a", newline="") as data:
            csv_nueva_entrada = csv.DictWriter(data, fieldnames=cls.COLUMNS)
            csv_nueva_entrada.writerow(nueva_entrada)

        print("✏️ Entrada nueva se registró de forma exitosa.")

    @classmethod
    def filtrar_entrada(cls, fecha_inicio, fecha_final):
        df = pd.read_csv(cls.CSV_FILE)
        df["fecha"] = pd.to_datetime(df["fecha"], format=cls.FORMAT)

        fecha_inicio = datetime.strptime(fecha_inicio, cls.FORMAT)
        fecha_final = datetime.strptime(fecha_final, cls.FORMAT)

        mask = (df["fecha"] >= fecha_inicio) & (df["fecha"] <= fecha_final)

        df_filtrado = df[mask]
        ingresos = df_filtrado.loc[df_filtrado["categoria"] == "Ingresos"]
        ingresos = ingresos["cantidad"].sum()

        egresos = df_filtrado.loc[df_filtrado["categoria"] == "Egresos"]
        egresos = egresos["cantidad"].sum()

        ahorros = ingresos - egresos

        if df_filtrado.empty:
            print("\n 🥲 No hay entradas durante esas fechas.")
        else:
            print(
                f"\n 📓Estado financiero durante {fecha_inicio.strftime(cls.FORMAT)} hasta {fecha_final.strftime(cls.FORMAT)}: "
            )
            print(df_filtrado.to_string(index=False))
            print(f"\n✌️ Ingresos = ${ingresos}")
            print(f"😭 Egresos = ${egresos}")
            print(f"💪 Ahorros = ${ahorros:.2f}")

        return ingresos, egresos, ahorros, df_filtrado


def recibir_entradas():
    fecha = obtener_fecha("Ingrese una fecha en formato válido (año-mes-día): ")
    cantidad = obtener_cantidad()
    categoria = obtener_categoria()
    descripcion = obtener_descripcion()

    CSV.agregar_entrada(
        fecha=fecha, cantidad=cantidad, categoria=categoria, descripcion=descripcion
    )


def crear_grafico(ingresos, egresos, ahorros):
    etiquetas = ["Ingresos", "Egresos", "Ahorros"]
    sizes = [ingresos, egresos, ahorros]
    explode = (0, 0.1, 0)

    if ahorros > 0:
        fig, ax = plt.subplots()  # Creamos la figura y los ejes.
        ax.pie(
            sizes,
            explode=explode,
            labels=etiquetas,
            autopct="%1.1f%%",
            shadow=True,
            startangle=90,
        )
        ax.axis("equal")
        return fig
    else:
        etiquetas = ["Ingresos", "Egresos"]
        sizes = [ingresos, egresos]
        explode = (0, 0.1)
        fig, ax = plt.subplots()  # Creamos la figura y los ejes.
        ax.pie(
            sizes,
            explode=explode,
            labels=etiquetas,
            autopct="%1.1f%%",
            shadow=True,
            startangle=90,
        )
        ax.axis("equal")
        return fig


def main():
    while True:
        print("\n1. 💵Ingresar entrada nueva: ")
        print("2. 💰Mostrar las entradas financieras ")
        print("3. 🚫Salir")
        eleccion = input("Seleccione una opción 1-3: ")

        if eleccion == "1":
            recibir_entradas()
        elif eleccion == "2":
            fecha_inicio = obtener_fecha(
                "Ingrese la fecha de inicio en el formato valido (año-mes-día)"
            )
            fecha_final = obtener_fecha(
                "Ingrese la fecha final en el formato valido (año-mes-día)"
            )
            ingresos, egresos, ahorros, df_filtrado = CSV.filtrar_entrada(
                fecha_inicio, fecha_final
            )
            ver_grafico = input("Desea ver un resumen gráfico S/N: ").upper()
            if ver_grafico == "S":
                crear_grafico(ingresos=ingresos, egresos=egresos, ahorros=ahorros)

        elif eleccion == "3":
            print("📊 Cerrando el programa...")
            break


if __name__ == "__main__":
    CSV.crear_csv_inicial()
    main()
