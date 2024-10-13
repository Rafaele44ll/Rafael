import os
os.system("cls")

hora_24 = int(input("Ingrese la hora en formato 24 horas (0-23): "))
minutos = int(input("Ingrese los minutos (0-59): "))

if 0 <= hora_24 <= 23 and 0 <= minutos <= 59:
    if hora_24 == 0:
        hora_12 = 12
        periodo = "AM"
    elif hora_24 < 12:
        hora_12 = hora_24
        periodo = "AM"
    elif hora_24 == 12:
        hora_12 = 12
        periodo = "PM"
    else:
        hora_12 = hora_24 - 12
        periodo = "PM"

    print(f"La hora en formato 12 horas es: {hora_12}:{minutos:02d} {periodo}")
else:
    print("Error: La hora o los minutos ingresados son inválidos.")
