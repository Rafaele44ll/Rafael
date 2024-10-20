import os
os.system("cls")

def verificar_cifras(numero, posicion=0, suma_pares=0, suma_impares=0):
    cifras = str(numero)

    if posicion == len(cifras):
        if suma_pares == suma_impares:
            print(numero)
            return 1
        return 0

    cifra = int(cifras[posicion])

    if cifra % 2 == 0:
        suma_pares += cifra
    else:
        suma_impares += cifra

    return verificar_cifras(numero, posicion + 1, suma_pares, suma_impares)

def encontrar_numeros():
    contador = 0
    for num in range(1000, 10000):  
        contador += verificar_cifras(num)
    return contador

cantidad = encontrar_numeros()
print(f"\nCantidad de números encontrados: {cantidad}.")
