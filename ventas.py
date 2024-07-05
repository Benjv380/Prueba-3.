import globales
import math
import random

def crear_venta():
    todos_los_productos = globales.leer_archivo_json('productos.json')
    ventas = globales.leer_archivo_json('ventas.json')
    id_venta = 0


    for venta in todos_los_productos:
        producto = random.choice(todos_los_productos)
        
        valor = random.randint(2,10) * 1000
        iva = valor*0.19
        id_venta += 1
        nueva_venta = {
            "":producto,
            "id_venta": id_venta,
            "valor": valor,
            "iva": iva
        }
        ventas.append(nueva_venta)
    globales.guardar_archivo_json('ventas.json', ventas)
    input("ventas cargadas")
