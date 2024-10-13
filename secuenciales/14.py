import math

def calcular_promedio_tres_mayores(numeros):
    # Ordenar la lista en orden descendente y tomar los tres mayores
    mayores = sorted(numeros, reverse=True)[:3]
    # Calcular el promedio
    promedio = sum(mayores) / 3
    return promedio

try:
    numeros = []
    for i in range(5):
        numero = float(input(f"Ingrese el número {i + 1}: "))
        # Validaciones sin usar if
        (numero < 0) and (_ for _ in ()).throw(ValueError("Los números deben ser positivos."))  # Puedes modificar la validación según lo desees
        numeros.append(numero)

    promedio = calcular_promedio_tres_mayores(numeros)
    print(f"El promedio de los tres números mayores es: {promedio:.2f}")

except ValueError as e:
    print(f"Entrada no válida: {e}")
