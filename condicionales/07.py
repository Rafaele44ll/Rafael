import os
os.system("cls")

num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
num3 = int(input("Ingrese el tercer número: "))

if (num1 > num2 and num1 < num3) or (num1 < num2 and num1 > num3):
    numero_intermedio = num1
elif (num2 > num1 and num2 < num3) or (num2 < num1 and num2 > num3):
    numero_intermedio = num2
else:
    numero_intermedio = num3

print(f"El número intermedio es: {numero_intermedio}")
