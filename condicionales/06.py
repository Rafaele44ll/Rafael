import os
os.system("cls")

edad1 = int(input("Ingrese la primera edad: "))
edad2 = int(input("Ingrese la segunda edad: "))
edad3 = int(input("Ingrese la tercera edad: "))

edad_menor = min(edad1, edad2, edad3)
edad_mayor = max(edad1, edad2, edad3)

print(f"La edad menor es: {edad_menor}")
print(f"La edad mayor es: {edad_mayor}")
