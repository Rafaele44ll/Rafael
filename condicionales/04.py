import os
os.system("cls")

def calcular_promedio(nota1, nota2, nota3):
    if nota3 >= 10:
        nota3 += 2  

    promedio_final = (nota1 + nota2 + nota3) / 3
    return promedio_final

nota1 = float(input("Ingrese la nota de la primera práctica: "))
nota2 = float(input("Ingrese la nota de la segunda práctica: "))
nota3 = float(input("Ingrese la nota de la tercera práctica: "))

promedio = calcular_promedio(nota1, nota2, nota3)
print(f"El promedio final del alumno es: {promedio:.2f}")
