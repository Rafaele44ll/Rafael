import os
os.system("cls")

def calcular_promedio_tres_mayores(numeros):
    
    mayores = sorted(numeros, reverse=True)[:3]

    promedio = sum(mayores) / 3
    return promedio

try:
    numeros = []
    for i in range(5):
        numero = float(input(f"Ingrese el número {i + 1}: "))

        (numero < 0) and (_ for _ in ()).throw(ValueError("Los números deben ser positivos."))  
        numeros.append(numero)

    promedio = calcular_promedio_tres_mayores(numeros)
    print(f"El promedio de los tres números mayores es: {promedio:.2f}")

except ValueError as e:
    print(f"Entrada no válida: {e}")
