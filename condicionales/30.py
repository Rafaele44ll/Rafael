import os
os.system("cls")

cuota = int(input("Ingrese la cuota mensual en dólares: "))
dia_pago = int(input("Ingrese el día de pago (1-30): "))

monto_a_pagar = cuota

if 1 <= dia_pago <= 10:

    descuento = max(5, 0.02 * cuota)
    monto_a_pagar -= descuento
elif 11 <= dia_pago <= 20:
   
    descuento = 0
else:
    # Recargo del mayor entre $10 y el 3% de la cuota
    recargo = max(10, 0.03 * cuota)
    monto_a_pagar += recargo

# Mostrar resultados
print("Monto a pagar:", monto_a_pagar)
