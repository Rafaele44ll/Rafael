def clasificar_angulo(angulo):
    
    if angulo == 0:
        return "Nulo"
    elif 0 < angulo < 90:
        return "Agudo"
    elif angulo == 90:
        return "Recto"
    elif 90 < angulo < 180:
        return "Obtuso"
    elif angulo == 180:
        return "Llano"
    elif 180 < angulo < 360:
        return "Cóncavo"
    elif angulo == 360:
        return "Completo"
    else:
        return "Ángulo no válido (fuera del rango 0° a 360°)"

try:
    angulo = float(input("Ingrese el ángulo en grados: "))
    
    
    (angulo < 0 or angulo > 360) and (_ for _ in ()).throw(ValueError("El ángulo debe estar en el rango de 0° a 360°."))

    clasificacion = clasificar_angulo(angulo)
    print(f"La clasificación del ángulo es: {clasificacion}")

except ValueError as e:
    print(f"Entrada no válida: {e}")
