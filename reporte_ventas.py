# Programa final: reporte de ventas de un producto

nombre_producto = input("Nombre del producto: ")
precio_compra = float(input("Precio de compra: "))
precio_venta = float(input("Precio de venta: "))
cantidad = int(input("Cantidad de productos vendidos: "))

costo_total = precio_compra * cantidad
ingreso_total = precio_venta * cantidad
ganancia = ingreso_total - costo_total

print()
print("----- REPORTE DE VENTAS -----")
print("Producto:", nombre_producto)
print("Precio de compra:", precio_compra)
print("Precio de venta:", precio_venta)
print("Cantidad vendida:", cantidad)
print("Costo total:", costo_total)
print("Ingreso total:", ingreso_total)
print("Ganancia:", ganancia)
print("-----------------------------")
