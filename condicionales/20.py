import os
os.system("cls")

a = int(input("Ingrese el primer número (a): "))
b = int(input("Ingrese el segundo número (b): "))
c = int(input("Ingrese el tercer número (c): "))

if a < b < c:
    orden = "ascendente"
elif a > b > c:
    orden = "descendente"
else:
    orden = "desordenado"

print(f"Los números fueron ingresados en orden {orden}.")
