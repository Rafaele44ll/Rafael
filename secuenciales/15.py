import os
os.system("cls")

juan = int(input("Ingrese el aporte de Juan en dólares (en centavos): "))
rosa = int(input("Ingrese el aporte de Rosa en dólares (en centavos): "))
daniel = int(input("Ingrese el aporte de Daniel en soles (en centavos): "))

dolar_a_soles = 300  
daniel_en_dolares = (daniel * 100) // dolar_a_soles  

capital_total = juan + rosa + daniel_en_dolares

porcentaje_juan = (juan * 100) // capital_total
porcentaje_rosa = (rosa * 100) // capital_total
porcentaje_daniel = (daniel_en_dolares * 100) // capital_total

print(f"Capital total en dólares: {capital_total // 100} USD")
print(f"Aporte de Juan: {porcentaje_juan}%")
print(f"Aporte de Rosa: {porcentaje_rosa}%")
print(f"Aporte de Daniel: {porcentaje_daniel}%")

