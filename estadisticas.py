import globales

def venta_mas_alta():
    todas_las_ventas = globales.guardar_archivo_json('ventas.json')
    ventas_ordenadas = sorted(todas_las_ventas, key=lambda x:x, ['ventas'], reverse=False)