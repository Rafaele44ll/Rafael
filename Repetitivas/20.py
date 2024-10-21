import os
os.system("cls")

def calcular_menor(numeros, indice=0, menor=float('inf')):
    if indice == len(numeros):
        return menor
    menor = min(menor, numeros[indice])
    return calcular_menor(numeros, indice + 1, menor)

def calcular_mayor(numeros, indice=0, mayor=float('-inf')):
    if indice == len(numeros):
        return mayor
    mayor = max(mayor, numeros[indice])
    return calcular_mayor(numeros, indice + 1, mayor)

def calcular_promedio(numeros, suma=0, indice=0):
    if indice == len(numeros):
        return suma / len(numeros) if len(numeros) > 0 else 0
    suma += numeros[indice]
    return calcular_promedio(numeros, suma, indice + 1)

numeros = []

for i in range(10):
    num = float(input(f"Introduce el número {i + 1}: "))
    numeros.append(num)

menor = calcular_menor(numeros)
mayor = calcular_mayor(numeros)
promedio = calcular_promedio(numeros)

print(f"Menor: {menor}")
print(f"Mayor: {mayor}")
print(f"Promedio: {promedio:.2f}")
