import os
os.system("cls")

numero1 = int(input("Ingrese el primer número (3 cifras): "))
numero2 = int(input("Ingrese el segundo número (3 cifras): "))

primera_cifra_num1 = numero1 // 100
segunda_cifra_num1 = (numero1 // 10) % 10
tercera_cifra_num1 = numero1 % 10

primera_cifra_num2 = numero2 // 100
segunda_cifra_num2 = (numero2 // 10) % 10
tercera_cifra_num2 = numero2 % 10

nuevo_numero1 = primera_cifra_num2 * 100 + segunda_cifra_num1 * 10 + tercera_cifra_num2
nuevo_numero2 = primera_cifra_num1 * 100 + segunda_cifra_num2 * 10 + tercera_cifra_num1

print(f"Número 1 intercambiado: {nuevo_numero1}")
print(f"Número 2 intercambiado: {nuevo_numero2}")
