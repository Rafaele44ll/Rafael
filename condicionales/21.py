import os
os.system("cls")

numero = int(input("Ingrese el número de cuatro cifras: "))

if 1000 <= numero < 10000:
    estado_civil = numero // 1000
    edad = (numero // 10) % 100
    sexo = numero % 10

    if estado_civil == 1:
        estado_civil_str = "Soltero"
    elif estado_civil == 2:
        estado_civil_str = "Casado"
    elif estado_civil == 3:
        estado_civil_str = "Divorciado"
    elif estado_civil == 4:
        estado_civil_str = "Viudo"
    else:
        estado_civil_str = "Estado civil no válido"

    if sexo == 1:
        sexo_str = "Masculino"
    elif sexo == 2:
        sexo_str = "Femenino"
    else:
        sexo_str = "Sexo no válido"

    print(f"Estado civil: {estado_civil_str}")
    print(f"Edad: {edad}")
    print(f"Sexo: {sexo_str}")
else:
    print("El número debe ser un entero positivo de cuatro cifras.")
