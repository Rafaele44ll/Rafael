import os
os.system("cls")

def suma_multiplos_3_no_5(n, actual=1):
    if actual > n:
        return 0
    
    if actual % 3 == 0 and actual % 5 != 0:
        return actual + suma_multiplos_3_no_5(n, actual + 1)
    
    return suma_multiplos_3_no_5(n, actual + 1)

n = int(input("Introduce un número entero (n): "))
resultado = suma_multiplos_3_no_5(n)
print(f"La suma de los múltiplos de 3 (no de 5) menores o iguales a {n} es: {resultado}.")
