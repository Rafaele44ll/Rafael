import os
os.system("cls")

numero = int(input("Ingrese un número de tres cifras: "))

centenas = numero // 100
decenas = (numero // 10) % 10
unidades = numero % 10

if (centenas + 1 == decenas and decenas + 1 == unidades) or (centenas - 1 == decenas and decenas - 1 == unidades):
    print("Las cifras son consecutivas.")
else:
    print("Las cifras no son consecutivas.")
