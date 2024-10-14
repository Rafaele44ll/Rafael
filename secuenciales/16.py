import os
os.system("cls")

horas_trabajadas = int(input("Ingrese el número total de horas trabajadas: "))
tarifa_horaria = int(input("Ingrese la tarifa horaria en soles: "))

sueldo_basico = horas_trabajadas * tarifa_horaria

bonificacion = sueldo_basico * 20 // 100
sueldo_bruto = sueldo_basico + bonificacion

descuento = sueldo_bruto * 10 // 100
sueldo_neto = sueldo_bruto - descuento

print("Sueldo básico:", sueldo_basico)
print("Sueldo bruto:", sueldo_bruto)
print("Sueldo neto:", sueldo_neto)

