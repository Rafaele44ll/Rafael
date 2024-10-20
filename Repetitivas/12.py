import os
os.system("cls")

def mostrar_numeros(n, limite=100):
    if n > limite:
        return
    print(n, end=' ')
    
    if n % 10 == 0:
        print()  

    mostrar_numeros(n + 1, limite)

mostrar_numeros(1)