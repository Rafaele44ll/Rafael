def calcular_sueldo(monto_vendido):
    sueldo_basico = 500
    comision_porcentaje = 0.09
    descuento_porcentaje = 0.11

    # Cálculo de la comisión
    comision = monto_vendido * comision_porcentaje

    # Cálculo del sueldo bruto
    sueldo_bruto = sueldo_basico + comision

    # Cálculo del descuento
    descuento = sueldo_bruto * descuento_porcentaje

    # Cálculo del sueldo neto
    sueldo_neto = sueldo_bruto - descuento

    return comision, sueldo_bruto, descuento, sueldo_neto


def validar_monto(monto_vendido):
    # Lanzar excepción si el monto vendido es negativo
    if monto_vendido < 0:
        raise ValueError("El monto vendido no puede ser negativo.")


try:
    monto_vendido = float(input("Ingrese el monto total vendido: "))
    validar_monto(monto_vendido)

    comision, sueldo_bruto, descuento, sueldo_neto = calcular_sueldo(monto_vendido)

    print(f"Comisión: S/. {comision:.2f}")
    print(f"Sueldo Bruto: S/. {sueldo_bruto:.2f}")
    print(f"Descuento: S/. {descuento:.2f}")
    print(f"Sueldo Neto: S/. {sueldo_neto:.2f}")
except ValueError as e:
    print(f"Entrada no válida: {e}")