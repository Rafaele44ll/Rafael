def convertir_unidades(metros):
    # Conversión a centímetros
    centimetros = metros * 100

    # Conversión a pulgadas
    pulgadas = centimetros / 2.54

    # Conversión a pies
    pies = pulgadas / 12

    # Conversión a yardas
    yardas = pies / 3

    return centimetros, pulgadas, pies, yardas


def validar_metros(metros):
    # Lanzar una excepción si metros es negativo
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