import os
os.system("cls")

def dibujar_rectangulo(n, altura_actual=0):
    if altura_actual == n:
        return
    print('*' * (2 * n))
    dibujar_rectangulo(n, altura_actual + 1)

n = int(input("Introduce la altura del rectángulo (n >= 4): "))

if n >= 4:
    dibujar_rectangulo(n)
else:
    print("La altura debe ser al menos 4.")
