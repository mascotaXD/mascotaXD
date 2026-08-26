# Programa que evalua una nota usando if, elif y else

nota = float(input("Ingresa tu nota: "))

if nota > 11:
    print("Aprobaste")
elif nota == 11:
    print("Estas justo en 11, revisa con tu profesor si aprobaste")
else:
    print("Desaprobaste")
