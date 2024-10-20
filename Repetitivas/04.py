import os
os.system("cls")

def mostrar_multiplos(n, m, contador=1):
    if contador > m:
        return
    else:
        print(n * contador)
        mostrar_multiplos(n, m, contador + 1)

n = int(input("Ingrese un número n: "))
m = int(input("Ingrese cuántos múltiplos desea mostrar (m): "))
mostrar_multiplos(n, m)
