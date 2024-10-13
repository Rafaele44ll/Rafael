def calcular_sueldo(num_horas, tarifa_horaria):
    # Cálculo del sueldo básico
    sueldo_basico = num_horas * tarifa_horaria
    
    # Cálculo de la bonificación del 20%
    bonificacion = sueldo_basico * 0.20
    sueldo_bruto = sueldo_basico + bonificacion
    
    # Cálculo del descuento del 10%
    descuento = sueldo_bruto * 0.10
    sueldo_neto = sueldo_bruto - descuento
    
    return sueldo_basico, sueldo_bruto, sueldo_neto

try:
    num_horas = float(input("Ingrese el número total de horas trabajadas: "))
    tarifa_horaria = float(input("Ingrese la tarifa horaria: "))
    
    # Validaciones sin usar if
    (num_horas < 0) and (_ for _ in ()).throw(ValueError("El número de horas no puede ser negativo."))
    (tarifa_horaria < 0) and (_ for _ in ()).throw(ValueError("La tarifa horaria no puede ser negativa."))
    
    sueldo_basico, sueldo_bruto, sueldo_neto = calcular_sueldo(num_horas, tarifa_horaria)
    
    print(f"Sueldo básico: S/. {sueldo_basico:.2f}")
    print(f"Sueldo bruto: S/. {sueldo_bruto:.2f}")
    print(f"Sueldo neto: S/. {sueldo_neto:.2f}")

except ValueError as e:
    print(f"Entrada no válida: {e}")
