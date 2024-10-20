import os
os.system("cls")

def tabla_multiplicar(n, x, y, i=None):
    if i is None:
        i = x  

    if i > y:
        return
    else:
        print(f"{n} x {i} = {n * i}")
        tabla_multiplicar(n, x, y, i + 1)

n = int(input("Ingrese un número n para generar su tabla de multiplicar: "))
x = int(input("Ingrese el valor mínimo x: "))
y = int(input("Ingrese el valor máximo y: "))
print(f"Tabla de multiplicar del {n} desde {x} hasta {y}:")
tabla_multiplicar(n, x, y)
