import os
os.system("cls")

monto_vendido = int(input("Ingrese el monto total vendido: "))

sueldo_base = (10 * monto_vendido) // 100

sueldo_adicional = 0
if monto_vendido > 5000:
    exceso = monto_vendido - 5000
    sueldo_adicional = (exceso // 500) * 25  

sueldo_total = sueldo_base + sueldo_adicional

print(f"Sueldo total del vendedor: S/. {sueldo_total}")
