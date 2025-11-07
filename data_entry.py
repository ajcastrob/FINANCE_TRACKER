from datetime import datetime

FORMATO = "%Y-%m-%d"
CATEGORIAS = {"I": "Ingresos", "E": "Egresos"}


def obtener_fecha(prompt, enter_key=False):
    fecha = input(prompt)
    if not fecha and not enter_key:
        fecha_actual = datetime.today()
        fecha_formateada = fecha_actual.strftime(FORMATO)
        print(fecha_formateada)
        return fecha_formateada

    try:
        fecha_usuario = datetime.strptime(fecha, FORMATO)
        fecha_formateada = fecha_usuario.strftime(FORMATO)
        return fecha_usuario
    except AttributeError:
        print("❌ Debe ingresar una fecha en el formato válido: ")
        return obtener_fecha(prompt, enter_key=False)
    except ValueError:
        print("❌ Debe ingresar una fecha en el formato válido: ")
        return obtener_fecha(prompt, enter_key=False)


def obtener_cantidad():
    cantidad = input("Ingrese la cantidad: $")

    try:
        cantidad = float(cantidad)
        if cantidad > 0:
            return cantidad
        else:
            print("La cantidad debe ser mayor a cero.")
            return obtener_cantidad()
    except ValueError:
        print("❌ Debe ingresar un número.")
        return obtener_cantidad()


def obtener_categoria():
    categoria = input("Ingrese la categoría 'I'(Ingresos) o 'E'(Egresos): ").upper()
    if categoria in CATEGORIAS.keys():
        print(CATEGORIAS[categoria])
        return CATEGORIAS[categoria]

    print("❌ Categoría inválida.")
    return obtener_categoria()


def obtener_descripcion():
    return input("Ingrese la descripción de la entrada: ")


# obtener_fecha("Ingrese una fecha en formato válido (año-mes-día): ")
# obtener_cantidad()
obtener_categoria()
obtener_descripcion()
