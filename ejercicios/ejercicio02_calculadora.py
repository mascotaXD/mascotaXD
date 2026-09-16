# Ejercicio 02: Calculadora

numero1 = float(input("Primer numero: "))
numero2 = float(input("Segundo numero: "))

suma = numero1 + numero2
resta = numero1 - numero2
multiplicacion = numero1 * numero2

print()
print("Suma:", suma)
print("Resta:", resta)
print("Multiplicacion:", multiplicacion)

if numero2 == 0:
    print("Division: no se puede dividir entre cero")
else:
    print("Division:", numero1 / numero2)
