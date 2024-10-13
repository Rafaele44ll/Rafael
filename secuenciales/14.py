import os
os.system("cls")

numero1 = int(input("Ingrese el número 1: "))
numero2 = int(input("Ingrese el número 2: "))
numero3 = int(input("Ingrese el número 3: "))
numero4 = int(input("Ingrese el número 4: "))
numero5 = int(input("Ingrese el número 5: "))

numeros = [numero1, numero2, numero3, numero4, numero5]

numeros.sort(reverse=True)

tres_mayores = numeros[0:3]

suma_tres_mayores = tres_mayores[0] + tres_mayores[1] + tres_mayores[2]
promedio = suma_tres_mayores / 3

print("Los tres números mayores son:", tres_mayores)
print("El promedio de los tres números mayores es:", promedio)

