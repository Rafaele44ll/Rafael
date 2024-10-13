import os
os.system("cls")

numero_tarjeta = int(input("Ingrese el número de la tarjeta: "))

monto_compra = float(input("Ingrese el monto de la compra: "))

if numero_tarjeta >= 100 and numero_tarjeta % 2 == 0:
    descuento = 0.15  # 15%
else:
    descuento = 0.05  # 5%
    
monto_descuento = monto_compra * descuento

print(f"Número de la tarjeta: {numero_tarjeta}")
print(f"Monto de la compra: ${monto_compra:.2f}")
print(f"Monto del descuento: ${monto_descuento:.2f}")
