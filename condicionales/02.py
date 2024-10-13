import os
os.system("cls")

precio = 20
unidades = int ( input ( "unidades: " ) )

compra = precio * unidades

if compra <= 500 : descuento = 0.12 * compra
elif compra <= 700 : descuento = 0.14 * compra
else : descuento = 0.16 * compra

if unidades <= 50 : caramelos = 5
elif unidades <= 100 : caramelos = 10 
else : caramelos = 15

print (f"compra = {compra:.2f}") 
print (f"descuento = {descuento:.2f}")
print (f"total = {(compra - descuento):.2f}")
print (f"caramelos = {caramelos:.2f}")

