import os
os.system("cls")

docenas = int(input("Ingrese la cantidad de docenas compradas: "))

precio_por_docena = float(input("Ingrese el precio por docena (en S/.): "))

monto_compra = docenas * precio_por_docena

if docenas >= 6:
    descuento = monto_compra * 0.15  
else:
    descuento = monto_compra * 0.10  

total_a_pagar = monto_compra - descuento

if docenas >= 30:
    lapiceros = (docenas // 3) * 2 
else:
    lapiceros = 0

print(f"Monto de la compra: S/. {monto_compra:.2f}")
print(f"Descuento: S/. {descuento:.2f}")
print(f"Total a pagar: S/. {total_a_pagar:.2f}")
print(f"Lapiceros de obsequio: {lapiceros}")
