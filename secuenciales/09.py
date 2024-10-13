import os
os.system("cls")

numero = int(input("Ingrese un número entero positivo de 4 cifras: "))

suma_cifras = 0

suma_cifras += (numero // 1000)        
suma_cifras += (numero // 100 % 10)      
suma_cifras += (numero // 10 % 10)       
suma_cifras += (numero % 10)             

print(f"La suma de las cifras es: {suma_cifras}")
