# Plan de Desarrollo del Proyecto: Finance Tracker (Pseudocódigo)

Este documento describe la lógica y el flujo del programa de seguimiento de finanzas.

## Fase 1: Inicialización y Menú Principal

```pseudocode
INICIO

  // 1. Configuración inicial
  FUNCIÓN inicializar():
    SI el archivo "finanzas.csv" no existe:
      Crear "finanzas.csv" con las cabeceras: "ID", "Fecha", "Tipo", "Categoria", "Monto", "Descripcion"
    FIN SI
  FIN FUNCIÓN

  // 2. Bucle principal de la aplicación
  FUNCIÓN menu_principal():
    LLAMAR A inicializar()
    
    MIENTRAS VERDADERO:
      Mostrar menú de opciones:
        1. Registrar nuevo movimiento (ingreso o gasto)
        2. Ver todos los movimientos
        3. Ver resumen de finanzas
        4. Salir

      Pedir al usuario que elija una opción

      SELECCIONAR SEGÚN la opción del usuario:
        CASO 1:
          LLAMAR A registrar_movimiento()
        CASO 2:
          LLAMAR A ver_movimientos()
        CASO 3:
          LLAMAR A ver_resumen()
        CASO 4:
          Mostrar mensaje de despedida
          SALIR del bucle
        CASO CONTRARIO:
          Mostrar mensaje de opción no válida
      FIN SELECCIONAR
    FIN MIENTRAS
  FIN FUNCIÓN

FIN
```

## Fase 2: Funcionalidades Detalladas

```pseudocode
// Registrar un nuevo ingreso o gasto
FUNCIÓN registrar_movimiento():
  Pedir al usuario el tipo de movimiento (Ingreso / Gasto)
  Pedir la categoría (Sueldo, Comida, Transporte, etc.)
  Pedir el monto
  Pedir una descripción (opcional)
  
  Obtener la fecha y hora actual
  Generar un ID único para el movimiento
  
  Validar que el monto sea un número positivo
  
  SI la validación es correcta:
    Crear una nueva fila con: ID, Fecha, Tipo, Categoria, Monto, Descripcion
    Añadir la nueva fila al archivo "finanzas.csv"
    Mostrar mensaje de éxito
  SINO:
    Mostrar mensaje de error en la validación
  FIN SI
FIN FUNCIÓN

// Mostrar todos los movimientos registrados
FUNCIÓN ver_movimientos():
  Leer el archivo "finanzas.csv"
  SI el archivo está vacío (aparte de las cabeceras):
    Mostrar mensaje "No hay movimientos registrados."
  SINO:
    Mostrar los datos del archivo en un formato de tabla claro y ordenado
  FIN SI
FIN FUNCIÓN

// Calcular y mostrar un resumen de las finanzas
FUNCIÓN ver_resumen():
  Leer el archivo "finanzas.csv"
  
  Inicializar total_ingresos = 0
  Inicializar total_gastos = 0
  
  PARA CADA fila en el archivo:
    SI el tipo es "Ingreso":
      total_ingresos = total_ingresos + monto de la fila
    SINO SI el tipo es "Gasto":
      total_gastos = total_gastos + monto de la fila
    FIN SI
  FIN PARA
  
  Calcular balance_final = total_ingresos - total_gastos
  
  Mostrar:
    - Total de Ingresos
    - Total de Gastos
    - Balance Final
FIN FUNCIÓN
```
