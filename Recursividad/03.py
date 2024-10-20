import os
os.system("cls")

def lista_inversa(n):
    if n == 0:
        return []
    return [n] + lista_inversa(n - 1)

resultado = lista_inversa(5)
print(resultado) 