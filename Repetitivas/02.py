import os
os.system("cls")

def multiplicar(a, b):
    # Caso base: si uno de los números es 0
    if b == 0:
        return 0
    # Si b es negativo, llamamos a la función con -b
    elif b < 0:
        return -multiplicar(a, -b)
    else:
        # Suma a con el resultado de multiplicar a por b-1
        return a + multiplicar(a, b - 1)

num1 = 5
num2 = 3
resultado = multiplicar(num1, num2)
print(f"{num1} multiplicado por {num2} es {resultado}")
