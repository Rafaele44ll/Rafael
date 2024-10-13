import os
os.system("cls")

def calcular_area_y_volumen(radio, altura):
    pi = 3.14  # Aproximación de π
    area = 2 * pi * radio * (radio + altura)
    volumen = pi * (radio ** 2) * altura
    return area, volumen

def obtener_valor(mensaje):
    while True:
        try:
            valor = float(input(mensaje))
            valor = valor * (valor >= 0)  
            return valor
        except ValueError:
            print("Entrada no válida. Intente nuevamente.")

radio = obtener_valor("Ingrese el radio del cilindro: ")
altura = obtener_valor("Ingrese la altura del cilindro: ")

area, volumen = calcular_area_y_volumen(radio, altura)

print(f"Área total del cilindro: {area:.2f} (usando π)")
print(f"Volumen del cilindro: {volumen:.2f} (usando π)")

