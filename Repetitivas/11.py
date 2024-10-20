import os
os.system("cls")

def es_capicua(numero):
    numero_str = str(numero)
    if len(numero_str) <= 1:
        return True
    if numero_str[0] == numero_str[-1]:
        return es_capicua(numero_str[1:-1])
    return False

def contar_capicuas(inicio, fin, contador=0):
    if inicio > fin:
        return contador
    if es_capicua(inicio):
        contador += 1
    return contar_capicuas(inicio + 1, fin, contador)

cantidad_capicuas = contar_capicuas(100, 999)
print(f"Cantidad de números capicúas de 3 cifras: {cantidad_capicuas}.")
