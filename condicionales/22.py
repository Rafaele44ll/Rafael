import os
os.system("cls")

cantidad_a = int(input("Ingrese la cantidad de unidades del producto A: "))
cantidad_b = int(input("Ingrese la cantidad de unidades del producto B: "))

precio_a = 25
precio_b = 30

importe_a = cantidad_a * precio_a
importe_b = cantidad_b * precio_b

descuento_a = 0
descuento_b = 0

if cantidad_a > 50:
    descuento_a = importe_a * 0.15  

if cantidad_b > 60:
    descuento_b = importe_b * 0.10  

importe_bruto = importe_a + importe_b
descuento_total = descuento_a + descuento_b
total_a_pagar = importe_bruto - descuento_total

print(f"Importe bruto: S/. {importe_bruto:.2f}")
print(f"Descuento: S/. {descuento_total:.2f}")
print(f"Total a pagar: S/. {total_a_pagar:.2f}")
