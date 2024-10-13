import os
os.system("cls")

pi = 3.14  

radio = float(input("Ingrese el radio del cilindro: "))
altura = float(input("Ingrese la altura del cilindro: "))

area_base = pi * (radio ** 2)
area_lateral = 2 * pi * radio * altura
area_total = 2 * area_base + area_lateral

print(area_base, area_lateral, area_total)

