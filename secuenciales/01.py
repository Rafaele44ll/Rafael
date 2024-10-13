def calcular_porcentajes(varones, mujeres):
    total_alumnos = varones + mujeres
    # Evitar división por cero
    return (total_alumnos > 0) * ((varones / total_alumnos) * 100), (total_alumnos > 0) * ((mujeres / total_alumnos) * 100)

try:
    total_alumnos = int(input("Ingrese la cantidad total de alumnos: "))
    
    # Validar y asignar valores usando excepciones
    (total_alumnos < 0) and (_ for _ in ()).throw(ValueError("La cantidad total de alumnos no puede ser negativa."))

    varones = int(input("Ingrese la cantidad de varones: "))
    mujeres = int(input("Ingrese la cantidad de mujeres: "))

    # Validación
    (varones < 0) and (_ for _ in ()).throw(ValueError("La cantidad de varones no puede ser negativa."))
    (mujeres < 0) and (_ for _ in ()).throw(ValueError("La cantidad de mujeres no puede ser negativa."))
    (varones + mujeres > total_alumnos) and (_ for _ in ()).throw(ValueError("La suma de varones y mujeres no puede exceder el total de alumnos."))

    porcentaje_varones, porcentaje_mujeres = calcular_porcentajes(varones, mujeres)
    print(f"Porcentaje de varones: {porcentaje_varones:.2f}%")
    print(f"Porcentaje de mujeres: {porcentaje_mujeres:.2f}%")
    
except ValueError as e:
    print(f"Entrada no válida: {e}")
