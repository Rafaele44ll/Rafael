import os
os.system("cls")

horas_trabajadas = int(input("Ingrese el número de horas trabajadas: "))
tarifa_por_hora = int(input("Ingrese la tarifa por hora en soles: "))

if horas_trabajadas <= 48:
    sueldo_bruto = horas_trabajadas * tarifa_por_hora
else:
    horas_extras = horas_trabajadas - 48
    sueldo_bruto = (48 * tarifa_por_hora) + (horas_extras * tarifa_por_hora * 1.2)

descuento = 0
if sueldo_bruto > 1500:
    descuento = sueldo_bruto * 11 // 100

total_a_pagar = sueldo_bruto - descuento

print("Horas trabajadas:", horas_trabajadas)
print("Pago por hora:", tarifa_por_hora)
print("Sueldo bruto:", sueldo_bruto)
print("Descuento:", descuento)
print("Total a pagar:", total_a_pagar)
