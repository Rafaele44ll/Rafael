import os
os.system("cls")

base = int(input("Ingrese la base del rectángulo: "))
altura = int(input("Ingrese la altura del rectángulo: "))

area = base * altura                  
perimetro = 2 * (base + altura)      

print(f"Área del rectángulo: {area}")
print(f"Perímetro del rectángulo: {perimetro}")
