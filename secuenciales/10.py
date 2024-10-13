def numero_al_reves(numero):
    # Convertir el número a cadena y revertirlo
    return str(numero)[::-1]

try:
    numero = int(input("Ingrese un número natural de 4 cifras: "))
    
    # Validaciones sin usar if
    (1000 <= numero < 10000) or (_ for _ in ()).throw(ValueError("El número debe tener 4 cifras."))
    
    resultado = numero_al_reves(numero)
    print(f"El número {numero} al revés es: {resultado}")

except ValueError as e:
    print(f"Entrada no válida: {e}")