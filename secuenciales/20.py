import os
os.system("cls")

def descomponer_cantidad(cantidad):
    billetes = [200, 100, 50, 20, 10]
    monedas = [5, 2, 1]

    descomposicion = {}

    for billete in billetes:
        if cantidad >= billete:
            cantidad_billetes = cantidad // billete
            descomposicion[billete] = cantidad_billetes
            cantidad -= cantidad_billetes * billete

    for moneda in monedas:
        if cantidad >= moneda:
            cantidad_monedas = cantidad // moneda
            descomposicion[moneda] = cantidad_monedas
            cantidad -= cantidad_monedas * moneda

    return descomposicion

cantidad = float(input("Ingrese la cantidad de dinero en soles: "))

if cantidad > 0:
    resultado = descomponer_cantidad(cantidad)
    print("Descomposición de la cantidad en billetes y monedas:")
    for denominacion, cantidad in resultado.items():
        print(f"{cantidad} de {denominacion} soles")
else:
    print("La cantidad debe ser un valor positivo.")
