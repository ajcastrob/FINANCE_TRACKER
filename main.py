import pandas as pd
import csv
from datetime import datetime


class CSV:
    # Crear una variable de clase
    CSV_FILE = "finance_data.csv"

    # Crear un método de clase para manejar la generación del csv.
    @classmethod
    def initialize_csv(cls):
        # Si existe lo cargamos.
        try:
            pd.read_csv(cls.CSV_FILE)
            # Crear el data frame si no existe.
        except FileNotFoundError:
            df = pd.DataFrame(
                columns=["Fecha", "Cantidad", "Categoría", "Descripcción"]
            )
            # Guardar el dataframe recién creado.
            df.to_csv(cls.CSV_FILE, index=False)


datos = CSV.initialize_csv()
