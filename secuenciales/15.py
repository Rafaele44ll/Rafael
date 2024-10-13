def calcular_capital_y_porcentajes(juan, rosa, daniel):
    # Conversión de soles a dólares
    daniel_en_dolares = daniel / 3.00
    
    # Capital total en dólares
    capital_total = juan + rosa + daniel_en_dolares
    
    # Cálculo de los porcentajes de cada uno
    porcentaje_juan = (juan / capital_total) * 100
    porcentaje_rosa = (rosa / capital_total) * 100
    porcentaje_daniel = (daniel_en_dolares / capital_total) * 100
    
    return capital_total, porcentaje_juan, porcentaje_rosa, porcentaje_daniel

try:
    juan = float(input("Ingrese el aporte de Juan en dólares: "))
    rosa = float(input("Ingrese el aporte de Rosa en dólares: "))
    daniel = float(input("Ingrese el aporte de Daniel en soles: "))
    
    # Validaciones sin usar if
    (juan < 0) and (_ for _ in ()).throw(ValueError("El aporte de Juan no puede ser negativo."))
    (rosa < 0) and (_ for _ in ()).throw(ValueError("El aporte de Rosa no puede ser negativo."))
    (daniel < 0) and (_ for _ in ()).throw(ValueError("El aporte de Daniel no puede ser negativo."))
    
    capital_total, porcentaje_juan, porcentaje_rosa, porcentaje_daniel = calcular_capital_y_porcentajes(juan, rosa, daniel)
    
    print(f"Capital total en dólares: {capital_total:.2f}")
    print(f"Porcentaje de Juan: {porcentaje_juan:.2f}%")
    print(f"Porcentaje de Rosa: {porcentaje_rosa:.2f}%")
    print(f"Porcentaje de Daniel: {porcentaje_daniel:.2f}%")

except ValueError as e:
    print(f"Entrada no válida: {e}")
