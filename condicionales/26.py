import os
os.system("cls")

monto_total = int(input("Ingrese el monto total de la compra: "))

porcentaje_prestamo = 0
monto_prestamo = 0
monto_propio = 0
interes = 0

if monto_total > 5000:
    porcentaje_prestamo = 30  
else:
    porcentaje_prestamo = 20  

monto_prestamo = (porcentaje_prestamo * monto_total) // 100

monto_propio = monto_total - monto_prestamo

interes = (10 * monto_prestamo) // 100  

print(f"Monto a pagar de su propio dinero: S/. {monto_propio}")
print(f"Monto del préstamo: S/. {monto_prestamo}")
print(f"Intereses del préstamo: S/. {interes}")
