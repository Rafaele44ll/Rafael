import os
os.system("cls")

def division_por_restas_sucesivas(dividendo, divisor, cociente=0):
    if dividendo < divisor:
        return cociente, dividendo
    else:
        return division_por_restas_sucesivas(dividendo - divisor, divisor, cociente + 1)

dividendo = 17
divisor = 4
cociente, resto = division_por_restas_sucesivas(dividendo, divisor)
print(f"Cociente: {cociente}, Resto: {resto}")
