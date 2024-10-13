import os
os.system("cls")

monto_vendido = int(input("Ingrese el monto total vendido: "))

sueldo_basico = 600

comision = (15 * monto_vendido) // 100
sueldo_bruto = sueldo_basico + comision

# Calcular el descuento
if sueldo_bruto > 1800:
    descuento = (10 * sueldo_bruto) // 100  
else:
    descuento = (5 * sueldo_bruto) // 100   

sueldo_neto = sueldo_bruto - descuento

if monto_vendido > 1000:
    polos_obsequiados = 3  

    polos_obsequiados = 1  

print(f"Sueldo bruto: S/. {sueldo_bruto}")
print(f"Descuento: S/. {descuento}")
print(f"Sueldo neto: S/. {sueldo_neto}")
print(f"Número de polos obsequiados: {polos_obsequiados}")
