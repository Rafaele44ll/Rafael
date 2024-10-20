import os
os.system("cls")

def contar_divisores(n, divisor=1):
    if divisor > n:
        return 0
    if n % divisor == 0:
        return 1 + contar_divisores(n, divisor + 1)
    else:
        return contar_divisores(n, divisor + 1)

numero = 12
cantidad_divisores = contar_divisores(numero)
print(f"La cantidad de divisores de {numero} es {cantidad_divisores}")
