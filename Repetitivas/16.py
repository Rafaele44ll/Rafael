import os
os.system("cls")

def invertir_cadena(cadena):
    if len(cadena) <= 1:
        return cadena
    
    return cadena[-1] + invertir_cadena(cadena[:-1])

texto = input("Introduce una cadena de texto: ")
cadena_invertida = invertir_cadena(texto)

print(f"Cadena invertida: {cadena_invertida}")
