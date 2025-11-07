import pandas as pd
import csv
from datetime import datetime


class CSV:
    """Una clase para manejar las operaciones del archivo CSV de finanzas"""

    CSV_FILE = "finance_personal_tracker.csv"
    COLUMNS = ["fecha", "monto", "categoria", "descripcion"]

    @classmethod
    def initialize_csv(cls):
        """Verifica si el archvio CSV existe. Si no, lo crea con las cabeceras definidas en cls.Columns"""
        try:
            pd.read_csv(cls.CSV_FILE)
        except FileNotFoundError:
            df = pd.DataFrame(columns=cls.COLUMNS)
            df.to_csv(cls.CSV_FILE, index=False)
            print("Creado el archivo de forma correcta.")

    @classmethod
    def add_entry(cls, fecha, monto, categoria, descripcion):
        new_entry = {
            "fecha": fecha,
            "monto": monto,
            "categoria": categoria,
            "descripcion": descripcion,
        }

        with open(cls.CSV_FILE, "a", newline="") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=cls.COLUMNS)
            writer.writerow(new_entry)

        print("Entrada guardada correctamente.")


CSV.initialize_csv()
