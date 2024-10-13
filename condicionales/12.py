import os
os.system("cls")

numero = int(input("Ingrese un número del 1 al 7: "))

if numero == 1:
    dia = "lunes"
elif numero == 2:
    dia = "martes"
elif numero == 3:
    dia = "miércoles"
elif numero == 4:
    dia = "jueves"
elif numero == 5:
    dia = "viernes"
elif numero == 6:
    dia = "sábado"
elif numero == 7:
    dia = "domingo"
else:
    dia = "Número inválido. Debe estar entre 1 y 7."

print(dia)
