import os
os.system("cls")

nota1 = int(input("Ingrese la primera nota: "))
nota2 = int(input("Ingrese la segunda nota: "))
nota3 = int(input("Ingrese la tercera nota: "))
nota4 = int(input("Ingrese la cuarta nota: "))
nota5 = int(input("Ingrese la quinta nota: "))

nota_mayor = max(nota1, nota2, nota3, nota4, nota5)
nota_menor = min(nota1, nota2, nota3, nota4, nota5)

print(f"Nota eliminada (mayor): {nota_mayor}")
print(f"Nota eliminada (menor): {nota_menor}")

promedio = (nota1 + nota2 + nota3 + nota4 + nota5 - nota_mayor - nota_menor) // 3

print(f"El promedio aprobatorio es: {promedio}")