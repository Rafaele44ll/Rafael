import os
os.system("cls")

def tabla_multiplicar(n, i=1):
    if i > 12:
        return
    else:
        print(f"{n} x {i} = {n * i}")
        tabla_multiplicar(n, i + 1)

n = int(input("Ingrese un número n para generar su tabla de multiplicar: "))
print(f"Tabla de multiplicar del {n}:")
tabla_multiplicar(n)
