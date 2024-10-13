import os
os.system("cls")

def clasificar_angulo(angulo):
    clasificacion = (
        (angulo == 0, "Nulo"),
        (0 < angulo < 90, "Agudo"),
        (angulo == 90, "Recto"),
        (90 < angulo < 180, "Obtuso"),
        (angulo == 180, "Llano"),
        (180 < angulo < 360, "Cóncavo"),
        (angulo == 360, "Completo")
    )
    
    for condicion, tipo in clasificacion:
        if condicion:
            return tipo
    
    return "Ángulo no válido (fuera del rango 0° a 360°)"

try:
    angulo = float(input("Ingrese el ángulo en grados: "))
    (angulo < 0 or angulo > 360) and (_ for _ in ()).throw(ValueError("El ángulo debe estar en el rango de 0° a 360°."))

    clasificacion = clasificar_angulo(angulo)
    print(f"La clasificación del ángulo es: {clasificacion}")

except ValueError as e:
    print(f"Entrada no válida: {e}")
