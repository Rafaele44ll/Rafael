import os
os.system("cls")

def formar_mayor_numero(num):
    cifras = [int(d) for d in str(num)]
    
    mayor = max(cifras)
    menor = min(cifras)

    mayor_numero = mayor * 10 + menor
    menor_numero = menor * 10 + mayor

    return mayor_numero, menor_numero

numero = int(input("Ingrese un número de 4 cifras: "))

if 1000 <= numero <= 9999:
    mayor_num, menor_num = formar_mayor_numero(numero)
    print(f"El mayor número posible de dos cifras es: {mayor_num}")
    print(f"El menor número posible de dos cifras es: {menor_num}")
else:
    print("El número ingresado no tiene 4 cifras.")
