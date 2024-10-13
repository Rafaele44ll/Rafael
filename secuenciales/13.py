import math

def calcular_hipotenusa(cateto_a, cateto_b):
    return math.sqrt(cateto_a**2 + cateto_b**2)

try:
    cateto_a = float(input("Ingrese la longitud del primer cateto: "))
    cateto_b = float(input("Ingrese la longitud del segundo cateto: "))
    
    (cateto_a < 0) and (_ for _ in ()).throw(ValueError("La longitud del cateto A no puede ser negativa."))
    (cateto_b < 0) and (_ for _ in ()).throw(ValueError("La longitud del cateto B no puede ser negativa."))
    
    hipotenusa = calcular_hipotenusa(cateto_a, cateto_b)
    print(f"La hipotenusa del triángulo es: {hipotenusa:.2f}")

except ValueError as e:
    print(f"Entrada no válida: {e}")
