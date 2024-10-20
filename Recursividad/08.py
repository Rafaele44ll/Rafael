import os
os.system("cls")

def contar_ocurrencias(lista, elemento):
    if not lista:
        return 0
    
    return (1 if lista[0] == elemento else 0) + contar_ocurrencias(lista[1:], elemento)

print(contar_ocurrencias([1, 2, 3, 1, 4, 1], 1))  