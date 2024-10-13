import os
os.system("cls")

sexo = input("Ingrese el sexo del postulante (F/M): ").upper()

edad = int(input("Ingrese la edad del postulante: "))

categoria = ""

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
    categoria = "Sexo no válido"

print(f"La categoría del postulante es: {categoria}")
