import os
os.system("cls")

ingreso_mensual = int(input("Ingrese el ingreso mensual del comprador (en S/.): "))

costo_casa = int(input("Ingrese el costo de la casa (en S/.): "))

if ingreso_mensual < 1250:
    cuota_inicial = (15 * costo_casa) // 100  
    monto_cuota_mensual = (costo_casa - cuota_inicial) // 120  
else:
    cuota_inicial = (30 * costo_casa) // 100  
    monto_cuota_mensual = (costo_casa - cuota_inicial) // 75  

print(f"Cuota inicial: S/. {cuota_inicial}")
print(f"Monto de la cuota mensual: S/. {monto_cuota_mensual}")
