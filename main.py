import pandas as pd
import csv
from datetime import datetime


class CSV:
    CSV_FILE = "finanzas_personales.csv"
    COLUMNS = ["fecha", "cantidad", "categoria", "descripcion"]

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


CSV.agregar_entrada("2025-15-10", 250, "Egresos", "Compras")
