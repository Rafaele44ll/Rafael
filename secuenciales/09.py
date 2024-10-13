import os
os.system("cls")

def suma_cifras(numero):

    return sum(int(digito) for digito in str(numero))

try:
    numero = int(input("Ingrese un número entero de 4 cifras: "))
    
    (1000 <= numero < 10000) or (_ for _ in ()).throw(ValueError("El número debe tener 4 cifras."))
    
    resultado = suma_cifras(numero)
    print(f"La suma de las cifras del número {numero} es: {resultado}")

except ValueError as e:
    print(f"Entrada no válida: {e}")