import os
os.system("cls")

num_varones = int(input("Ingrese el número de varones en el salón: "))
num_mujeres = int(input("Ingrese el número de mujeres en el salón: "))

total_estudiantes = num_varones + num_mujeres

porcentaje_varones = (num_varones * 100) // (total_estudiantes + (total_estudiantes == 0))
porcentaje_mujeres = (num_mujeres * 100) // (total_estudiantes + (total_estudiantes == 0))

print(f"Porcentaje de varones: {porcentaje_varones}%")
print(f"Porcentaje de mujeres: {porcentaje_mujeres}%")
