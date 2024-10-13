import math

def calcular_area_y_volumen(radio, altura):
    # Cálculo del área total
    area = 2 * math.pi * radio * (radio + altura)
    
    # Cálculo del volumen
    volumen = math.pi * (radio ** 2) * altura
    
    return area, volumen

try:
    radio = float(input("Ingrese el radio del cilindro: "))
    altura = float(input("Ingrese la altura del cilindro: "))
    
    # Validaciones sin usar if
    (radio < 0) and (_ for _ in ()).throw(ValueError("El radio no puede ser negativo."))
    (altura < 0) and (_ for _ in ()).throw(ValueError("La altura no puede ser negativa."))
    
    area, volumen = calcular_area_y_volumen(radio, altura)
    
    print(f"Área total del cilindro: {area:.2f}")
    print(f"Volumen del cilindro: {volumen:.2f}")

except ValueError as e:
    print(f"Entrada no válida: {e}")
