# Ejercicio 07: Promedio con funcion

def calcular_promedio(n1, n2, n3):
    return (n1 + n2 + n3) / 3


nota1 = float(input("Nota 1: "))
nota2 = float(input("Nota 2: "))
nota3 = float(input("Nota 3: "))

promedio = calcular_promedio(nota1, nota2, nota3)

print()
print("El promedio es:", round(promedio, 2))

if promedio >= 11:
    print("El estudiante aprobo")
else:
    print("El estudiante desaprobo")
