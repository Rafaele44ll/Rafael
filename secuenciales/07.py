def calcular_area_y_perimetro(base, altura):
    # Cálculo del área
    area = base * altura
    
    # Cálculo del perímetro
    perimetro = 2 * (base + altura)
    
    return area, perimetro

try:
    base = float(input("Ingrese la base del rectángulo: "))
    altura = float(input("Ingrese la altura del rectángulo: "))
    
    # Validaciones sin usar if
    (base < 0) and (_ for _ in ()).throw(ValueError("La base no puede ser negativa."))
    (altura < 0) and (_ for _ in ()).throw(ValueError("La altura no puede ser negativa."))
    
    area, perimetro = calcular_area_y_perimetro(base, altura)
    
    print(f"Área del rectángulo: {area:.2f}")
    print(f"Perímetro del rectángulo: {perimetro:.2f}")

except ValueError as e:
    print(f"Entrada no válida: {e}")
