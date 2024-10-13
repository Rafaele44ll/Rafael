import math

def calcular_ecuacion_segundo_grado(a, b, c):
    # Calcular el discriminante
    discriminante = b**2 - 4*a*c
    
    # Calcular las soluciones basadas en el discriminante
    raiz1 = (-b + math.sqrt(discriminante)) / (2 * a)
    raiz2 = (-b - math.sqrt(discriminante)) / (2 * a)
    
    return raiz1, raiz2

try:
    a = float(input("Ingrese el coeficiente a (no puede ser 0): "))
    b = float(input("Ingrese el coeficiente b: "))
    c = float(input("Ingrese el coeficiente c: "))
    
    # Validaciones sin usar if
    (a == 0) and (_ for _ in ()).throw(ValueError("El coeficiente a no puede ser 0."))
    
    discriminante = b**2 - 4*a*c
    (discriminante < 0) and (_ for _ in ()).throw(ValueError("No hay soluciones reales, el discriminante es negativo."))
    
    raiz1, raiz2 = calcular_ecuacion_segundo_grado(a, b, c)
    print(f"Las raíces de la ecuación son: {raiz1:.2f} y {raiz2:.2f}")

except ValueError as e:
    print(f"Entrada no válida: {e}")
