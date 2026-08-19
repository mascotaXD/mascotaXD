# Programa simple para calcular los ingresos de un producto

costo_produccion = float(input("Costo de produccion por unidad: "))
precio_venta = float(input("Precio de venta por unidad: "))
cantidad_vendida = int(input("Cantidad vendida: "))

ingresos = precio_venta * cantidad_vendida
costo_total = costo_produccion * cantidad_vendida
ganancia = ingresos - costo_total

print("El costo total de produccion fue:", costo_total)
print("Tus ingresos son:", ingresos)
print("Tu ganancia es:", ganancia)
