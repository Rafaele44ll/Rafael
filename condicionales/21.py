import os
os.system("cls")

numero = int(input("Ingrese el número de cuatro cifras: "))

if 1000 <= numero < 10000:
    estado_civil = numero // 1000
    edad = (numero // 10) % 100
    sexo = numero % 10

    if estado_civil == 1:
        estado_civil_resultado = "Soltero"
    elif estado_civil == 2:
        estado_civil_resultado = "Casado"
    elif estado_civil == 3:
        estado_civil_resultado = "Divorciado"
    elif estado_civil == 4:
        estado_civil_resultado = "Viudo"
    else:
        estado_civil_resultado = "Estado civil no válido"

    if sexo == 1:
        sexo_resultado = "Masculino"
    elif sexo == 2:
        sexo_resultado = "Femenino"
    else:
        sexo_resultado = "Sexo no válido"

    print("Estado civil:", estado_civil_resultado)
    print("Edad:", edad)
    print("Sexo:", sexo_resultado)
else:
    print("El número debe ser un entero positivo de cuatro cifras.")
