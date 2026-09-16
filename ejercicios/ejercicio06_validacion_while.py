# Ejercicio 06: Validacion con while

CLAVE_CORRECTA = "python123"

contrasena = input("Ingresa la contrasena: ")

while contrasena != CLAVE_CORRECTA:
    print("Contrasena incorrecta. Intenta nuevamente.")
    contrasena = input("Ingresa la contrasena: ")

print("Acceso permitido!")
