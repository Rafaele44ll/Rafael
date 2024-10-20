import os
os.system("cls")

def permutaciones(cadena):
    if len(cadena) == 1:
        return [cadena]
    
    resultado = []
    for i, letra in enumerate(cadena):
        subcadena = cadena[:i] + cadena[i+1:]
        for perm in permutaciones(subcadena):
            resultado.append(letra + perm)
    
    return resultado

print(permutaciones("abc")) 