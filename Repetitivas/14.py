import os
os.system("cls")

def es_primo(n, divisor=None):
    if n < 2:
        return False
    if divisor is None:
        divisor = n - 1
    if divisor == 1:
        return True
    if n % divisor == 0:
        return False
    return es_primo(n, divisor - 1)

numero = int(input("Introduce un número entero: "))
if es_primo(numero):
    print(f"{numero} es un número primo.")
else:
    print(f"{numero} no es un número primo.")
