import os
os.system("cls")

import os
os.system("cls")

def invertir_cadena(cadena):
    if len(cadena) <= 1:
        return cadena
    
    return cadena[-1] + invertir_cadena(cadena[:-1])

texto = "hola"
resultado = invertir_cadena(texto)
print(resultado)  