from csv_file import CSV
from data_entry import (
    obtener_cantidad,
    obtener_categoria,
    obtener_descripcion,
    obtener_fecha,
)
from graficos.graficos import crear_grafico


def recibir_entradas():
    fecha = obtener_fecha("Ingrese una fecha en formato válido (año-mes-día): ")
    cantidad = obtener_cantidad()
    categoria = obtener_categoria()
    descripcion = obtener_descripcion()

    CSV.agregar_entrada(
        fecha=fecha, cantidad=cantidad, categoria=categoria, descripcion=descripcion
    )


def cli():
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
    cli()
