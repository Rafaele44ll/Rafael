def descomponer_dinero(cantidad):
    # Billetes y monedas disponibles
    billetes_y_monedas = {
        200: 0,
        100: 0,
        50: 0,
        20: 0,
        10: 0,
        5: 0,
        2: 0,
        1: 0
    }
    
    # Descomposición
    for billete in billetes_y_monedas.keys():
        billetes_y_monedas[billete], cantidad = divmod(cantidad, billete)
    
    return billetes_y_monedas

def validar_cantidad(cantidad):
    # Lanzar excepción si la cantidad es negativa
    (cantidad < 0) and (_ for _ in ()).throw(ValueError("La cantidad de dinero no puede ser negativa."))

try:
    cantidad = float(input("Ingrese la cantidad de dinero en soles: "))
    
    # Validar sin usar if
    validar_cantidad(cantidad)

    resultado = descomponer_dinero(cantidad)
    
    print("Descomposición de la cantidad:")
    [print(f"{cantidad} billete(s)/moneda(s) de S/. {billete}") for billete, cantidad in resultado.items() if cantidad > 0]

except ValueError as e:
    print(f"Entrada no válida: {e}")
