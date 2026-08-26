# Programa que muestra un mensaje segun el rango de la nota

nota = int(input("Ingresa tu nota (0 a 20): "))

if nota < 0 or nota > 20:
    print("Nota invalida, debe estar entre 0 y 20")
elif nota >= 18:
    print("Excelente")
elif nota >= 14:
    print("Buen trabajo")
elif nota >= 11:
    print("Aprobado")
else:
    print("Desaprobado")
