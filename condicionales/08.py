import os
os.system("cls")

propina_base = 20

examenes_aprobados = int(input("Ingrese la cantidad de exámenes aprobados (0-3): "))

if 0 <= examenes_aprobados <= 3:
    propina_adicional = examenes_aprobados * 5

    total_propina = propina_base + propina_adicional

    print(f"El monto total de la propina es: S/. {total_propina}")
else:
    print("La cantidad de exámenes aprobados debe estar entre 0 y 3.")
