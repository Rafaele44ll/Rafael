import os
os.system("cls")

sexo = input("Ingrese el sexo del postulante (F/M): ")

edad = int(input("Ingrese la edad del postulante: "))

if sexo == "F":
    if edad < 23:
        categoria = "FA"
    else:
        categoria = "FB"
elif sexo == "M":
    if edad < 25:
        categoria = "MA"
    else:
        categoria = "MB"
else:
    categoria = "Inválido"

print("Categoría:", categoria)
