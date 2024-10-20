import os
os.system("cls")

def esta_ordenada(lista):
    if len(lista) <= 1:
        return True
    return lista[0] <= lista[1] and esta_ordenada(lista[1:])

resultado = esta_ordenada([1, 2, 3, 4, 5])
print(resultado) 