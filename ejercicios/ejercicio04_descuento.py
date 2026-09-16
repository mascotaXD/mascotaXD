# Ejercicio 04: Descuento

monto = float(input("Monto de compra (S/): "))

if monto >= 200:
    porcentaje = 15
elif monto >= 100:
    porcentaje = 10
elif monto >= 50:
    porcentaje = 5
else:
    porcentaje = 0

descuento = monto * porcentaje / 100
total_pagar = monto - descuento

print()
print("Monto de compra: S/", round(monto, 2))
print("Descuento:", porcentaje, "%")
print("Monto descontado: S/", round(descuento, 2))
print("Total a pagar: S/", round(total_pagar, 2))
