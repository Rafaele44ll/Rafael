import os
os.system("cls")

def a_mayusculas(cadena):
    if not cadena:
        return ""
    
    return cadena[0].upper() + a_mayusculas(cadena[1:])

def a_minusculas(cadena):
    if not cadena:
        return ""
    
    return cadena[0].lower() + a_minusculas(cadena[1:])
texto = input("Introduce una cadena de texto: ")

texto_mayusculas = a_mayusculas(texto)
texto_minusculas = a_minusculas(texto)

print(f"Texto en mayúsculas: {texto_mayusculas}")
print(f"Texto en minúsculas: {texto_minusculas}")
