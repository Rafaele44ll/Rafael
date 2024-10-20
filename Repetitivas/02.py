import os
os.system("cls")

def multiplicar(a, b):
    if b == 0:
        return 0
    elif b < 0:
        return -multiplicar(a, -b)
    else:
        return a + multiplicar(a, b - 1)

num1 = 5
num2 = 3
resultado = multiplicar(num1, num2)
print(f"{num1} multiplicado por {num2} es {resultado}")
