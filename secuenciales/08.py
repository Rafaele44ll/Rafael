import math

def calcular_area_cilindro(radio, altura):

    area_base = math.pi * (radio ** 2)
    
    area_lateral = 2 * math.pi * radio * altura
    
    area_total = 2 * area_base + area_lateral
    
    return area_base, area_lateral, area_total

try:
    radio = float(input("Ingrese el radio del cilindro: "))
    altura = float(input("Ingrese la altura del cilindro: "))
    
    # Validaciones sin usar if
    (radio < 0) and (_ for _ in ()).throw(ValueError("El radio no puede ser negativo."))
    (altura < 0) and (_ for _ in ()).throw(ValueError("La altura no puede ser negativa."))
    
    area_base, area_lateral, area_total = calcular_area_cilindro(radio, altura)
    
    print(f"Área base del cilindro: {area_base:.2f}")
    print(f"Área lateral del cilindro: {area_lateral:.2f}")
    print(f"Área total del cilindro: {area_total:.2f}")

except ValueError as e:
    print(f"Entrada no válida: {e}")
