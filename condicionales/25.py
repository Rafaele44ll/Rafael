import os
os.system("cls")

sueldo_bruto = int(input("Ingrese el sueldo bruto del empleado: "))

numero_hijos = int(input("Ingrese el número de hijos del empleado: "))

if numero_hijos > 1:
    bonificacion = (12.5 * sueldo_bruto) // 100 + (numero_hijos * 40)  
else:
    bonificacion = sueldo_bruto * 10 // 100  

sueldo_neto = sueldo_bruto + bonificacion

print(f"Bonificación: S/. {bonificacion}")
print(f"Sueldo neto a pagar: S/. {sueldo_neto}")
