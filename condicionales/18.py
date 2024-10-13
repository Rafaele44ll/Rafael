import os
os.system("cls")

donacion = int(input("Ingrese el monto de la donación (en $): "))

centro_salud = 0
comedor_ninos = 0
inversion_bolsa = 0

if donacion >= 10000:
    centro_salud = (30 * donacion) // 100  
    comedor_ninos = (50 * donacion) // 100  
else:
    centro_salud = (25 * donacion) // 100  
    comedor_ninos = (60 * donacion) // 100  

inversion_bolsa = donacion - (centro_salud + comedor_ninos)

print(f"Monto destinado al centro de salud: ${centro_salud}")
print(f"Monto destinado al comedor de niños: ${comedor_ninos}")
print(f"Monto invertido en la bolsa: ${inversion_bolsa}")
