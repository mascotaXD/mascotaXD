# Programa que indica si la persona puede votar segun su edad

edad = int(input("Ingresa tu edad: "))

if edad >= 18:
    print("Puede votar")
else:
    faltan = 18 - edad
    print("Aun no puede votar")
    print("Te faltan", faltan, "anios para cumplir 18")
