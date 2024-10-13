def determinar_signo(numero):
    if numero > 0:
        return "El número es positivo."
    elif numero < 0:
        return "El número es negativo."
    else:
        return "El número es cero."

try:
    # Solicitar al usuario que ingrese un número
    numero = float(input("Ingrese un número: "))
    
    # Determinar el signo del número
    resultado = determinar_signo(numero)
    
    # Mostrar el resultado
    print(resultado)

except ValueError:
    print("Entrada no válida. Por favor, ingrese un número.")
