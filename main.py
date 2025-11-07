import pandas as pd
import csv
from datetime import datetime


class CSV:
    CSV_FILE = "finanzas_personales.csv"
    COLUMNS = ["fecha", "cantidad", "clasificacion", "descripcion"]

    @classmethod
    def crear_csv_inicial(cls):
        try:
            df = pd.read_csv(cls.CSV_FILE)
            print("📈 Finanzas personales: ")
            print(df.to_string())
        except FileNotFoundError:
            df = pd.DataFrame(columns=cls.COLUMNS)
            df.to_csv(cls.CSV_FILE, index=False)
            print("🗒️ Archivo creado con éxito.")


CSV.crear_csv_inicial()
