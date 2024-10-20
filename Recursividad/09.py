import os
os.system("cls")

def es_palindromo(cadena):
    cadena = cadena.lower()  
    if len(cadena) <= 1:
        return True
    if cadena[0] != cadena[-1]:
        return False
    return es_palindromo(cadena[1:-1])

print(es_palindromo("Anita lava la tina"))  
print(es_palindromo("Hola"))   