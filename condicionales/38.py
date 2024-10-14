import os
os.system("cls")

def es_bisiesto(año):
    return (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0)

mes = int(input("Ingrese el número del mes (1-12): "))
año = int(input("Ingrese el año: "))

nombre_mes = ""
dias = 0

if mes == 1:
    nombre_mes = "Enero"
    dias = 31
elif mes == 2:
    nombre_mes = "Febrero"
    dias = 29 if es_bisiesto(año) else 28
elif mes == 3:
    nombre_mes = "Marzo"
    dias = 31
elif mes == 4:
    nombre_mes = "Abril"
    dias = 30
elif mes == 5:
    nombre_mes = "Mayo"
    dias = 31
elif mes == 6:
    nombre_mes = "Junio"
    dias = 30
elif mes == 7:
    nombre_mes = "Julio"
    dias = 31
elif mes == 8:
    nombre_mes = "Agosto"
    dias = 31
elif mes == 9:
    nombre_mes = "Septiembre"
    dias = 30
elif mes == 10:
    nombre_mes = "Octubre"
    dias = 31
elif mes == 11:
    nombre_mes = "Noviembre"
    dias = 30
elif mes == 12:
    nombre_mes = "Diciembre"
    dias = 31
else:
    nombre_mes = "Mes no válido"

if dias > 0:
    print(f"El mes de {nombre_mes} tiene {dias} días.")
else:
    print(nombre_mes)