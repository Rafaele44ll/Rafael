import os
os.system("cls")

sueldo_basico = 500

monto_vendido = int(input("Ingrese el monto total vendido en soles: "))

comision = monto_vendido * 9 // 100

sueldo_bruto = sueldo_basico + comision

descuento = sueldo_bruto * 11 // 100

sueldo_neto = sueldo_bruto - descuento

print("Comisión:", comision)
print("Sueldo bruto:", sueldo_bruto)
print("Descuento:", descuento)
print("Sueldo neto:", sueldo_neto)
