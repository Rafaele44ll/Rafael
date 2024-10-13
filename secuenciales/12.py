import os
os.system("cls")

a = int(input("Ingrese el coeficiente a (entero): "))
b = int(input("Ingrese el coeficiente b (entero): "))
c = int(input("Ingrese el coeficiente c (entero): "))

discriminante = b**2 - 4*a*c

raiz1 = (-b + int(discriminante**0.5)) // (2 * a)
raiz2 = (-b - int(discriminante**0.5)) // (2 * a)

print("Raíz 1:", raiz1)
print("Raíz 2:", raiz2)
