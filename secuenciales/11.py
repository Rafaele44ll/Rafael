import os
os.system("cls")

def intercambiar_cifras(num1, num2):
    str_num1 = str(num1)
    str_num2 = str(num2)
    
    nuevo_num1 = str_num2[0] + str_num1[1] + str_num2[2]
    nuevo_num2 = str_num1[0] + str_num2[1] + str_num1[2]
    
    return int(nuevo_num1), int(nuevo_num2)

try:
    num1 = int(input("Ingrese el primer número de 3 cifras: "))
    num2 = int(input("Ingrese el segundo número de 3 cifras: "))
    
    (100 <= num1 < 1000) or (_ for _ in ()).throw(ValueError("El primer número debe tener 3 cifras."))
    (100 <= num2 < 1000) or (_ for _ in ()).throw(ValueError("El segundo número debe tener 3 cifras."))
    
    resultado1, resultado2 = intercambiar_cifras(num1, num2)
    print(f"Nuevos números: {resultado1} y {resultado2}")

except ValueError as e:
    print(f"Entrada no válida: {e}")
