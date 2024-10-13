import os
os.system("cls")

def determinar_signo(numero):
    if numero > 0:
        return "El número es positivo."
    elif numero < 0:
        return "El número es negativo."
    else:
        return "El número es cero."

try:
    numero = float(input("Ingrese un número: "))
    
    resultado = determinar_signo(numero)
    
    print(resultado)

except ValueError:
    print("Entrada no válida. Por favor, ingrese un número.")
