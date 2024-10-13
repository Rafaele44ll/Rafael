import os
os.system("cls")

donacion_total = int(input("Ingrese el monto total de la donación: "))

centro_salud = donacion_total * 25 // 100
comedor_infantil = donacion_total * 35 // 100
escuela_infantil = donacion_total * 25 // 100
asilo_ancianos = donacion_total * 15 // 100  

print(centro_salud, comedor_infantil, escuela_infantil, asilo_ancianos)
