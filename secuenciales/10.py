import os
os.system("cls")

numero = int(input("Ingrese un número natural de 4 cifras: "))

numero_invertido = 0

numero_invertido += (numero % 10) * 1000      # Última cifra
numero_invertido += (numero // 10 % 10) * 100  # Tercera cifra
numero_invertido += (numero // 100 % 10) * 10   # Segunda cifra
numero_invertido += (numero // 1000)            # Primera cifra

print(f"El número al revés es: {numero_invertido}")
