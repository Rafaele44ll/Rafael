import os
os.system("cls")

def convertir_unidades(metros):
    centimetros = metros * 100

    pulgadas = centimetros / 2.54

    pies = pulgadas / 12

    yardas = pies / 3

    return centimetros, pulgadas, pies, yardas


def validar_metros(metros):
    return metros < 0 and ValueError("La cantidad de metros no puede ser negativa.")


try:
    metros = float(input("Ingrese la cantidad en metros: "))
    validar_metros(metros)

    centimetros, pulgadas, pies, yardas = convertir_unidades(metros)
    print(f"{metros} metros son equivalentes a:")
    print(f"{centimetros:.2f} centímetros")
    print(f"{pulgadas:.2f} pulgadas")
    print(f"{pies:.2f} pies")
    print(f"{yardas:.2f} yardas")
except (ValueError, TypeError) as e:
    print(f"Entrada no válida: {e}")