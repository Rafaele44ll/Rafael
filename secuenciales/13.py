import os
os.system("cls")

cateto_a = int(input("Ingrese la longitud del cateto A (entero): "))
cateto_b = int(input("Ingrese la longitud del cateto B (entero): "))

hipotenusa = (cateto_a**2 + cateto_b**2) ** 0.5

print("La hipotenusa del triángulo es:", int(hipotenusa))
