import os
os.system("cls")

def potencia(n, m):
    if m == 0:
        return 1
    else:
        return n * potencia(n, m - 1)

base = float(input("Introduce la base (n): "))
exponente = int(input("Introduce el exponente (m): "))

resultado = potencia(base, exponente)
print(f"{base} elevado a la {exponente} es {resultado}.")
