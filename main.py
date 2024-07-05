import globales
import ventas

def menu_general():
    print("1. Asignar montos aleatorios")
    print("2. Estadisticas")
    print("3. Salir")

    opcion = globales.seleccionar_opcion(3)

    while True:
        if opcion == 1:
            ventas.crear_venta()
            input()
        elif opcion == 2:
            print("esta")
            input()
        elif opcion == 3:
            return
        input()

menu_general()
