import pandas as pd
import csv
from datetime import datetime
import streamlit as st


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

        return ingresos, egresos, ahorros, df_filtrado
