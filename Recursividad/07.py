import os
os.system("cls")

def max_lista(lista):
    if len(lista) == 1:
        return lista[0]
    
    max_resto = max_lista(lista[1:])
    return lista[0] if lista[0] > max_resto else max_resto

print(max_lista([3, 1, 4, 1, 5, 9, 2]))  