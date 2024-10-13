def calcular_total(cantidad):
    if 1 <= cantidad <= 25:
        precio_unitario = 27
    elif 26 <= cantidad <= 50:
        precio_unitario = 25
    elif cantidad >= 51:
        precio_unitario = 23
    else:
        return "Cantidad no válida"

    importe = cantidad * precio_unitario

    if cantidad > 50:
        descuento = importe * 0.15
    else:
        descuento = importe * 0.05

    total_a_pagar = importe - descuento

    return importe, descuento, total_a_pagar

cantidad = int(input("Ingrese la cantidad de unidades: "))
resultado = calcular_total(cantidad)

if isinstance(resultado, str):
    print(resultado)
else:
    importe, descuento, total_a_pagar = resultado
    print(f"Importe de la compra: S/. {importe:.2f}")
    print(f"Descuento: S/. {descuento:.2f}")
    print(f"Total a pagar: S/. {total_a_pagar:.2f}")
