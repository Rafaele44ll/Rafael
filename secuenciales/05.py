import os
os.system("cls")

def formar_mayor_numero(num):
    digitos = [int(d) for d in str(num)]
    
    cifra_mayor = max(digitos)
    cifra_menor = min(digitos)
    
    numero1 = cifra_mayor * 10 + cifra_menor  
    numero2 = cifra_menor * 10 + cifra_mayor  
    
    return numero1, numero2

try:
    numero = int(input("Ingrese un número de 4 cifras: "))
    
    (1000 <= numero < 10000) or (_ for _ in ()).throw(ValueError("El número debe tener 4 cifras."))

    mayor, menor = formar_mayor_numero(numero)
    print(f"El mayor número posible de dos cifras es: {mayor}")
    print(f"El menor número posible de dos cifras es: {menor}")

except ValueError as e:
    print(f"Entrada no válida: {e}")
