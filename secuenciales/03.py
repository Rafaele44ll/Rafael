import os
os.system("cls")

def convertir_a_metros(kilometros, pies, millas):
    
    metros_kilometros = kilometros * 1000
    
    metros_pies = pies / 3.2808
    
    metros_millas = millas * 1609
    
    total_metros = metros_kilometros + metros_pies + metros_millas
    
    return total_metros

def metros_a_yardas(metros):
    return metros / 0.9144  

try:
    kilometros = float(input("Ingrese la longitud del primer tramo en kilómetros: "))
    pies = int (input("Ingrese la longitud del segundo tramo en pies: "))
    millas = int (input("Ingrese la longitud del tercer tramo en millas: "))
    
    total_metros = convertir_a_metros(kilometros, pies, millas)
    
    total_yardas = metros_a_yardas(total_metros)
    
    print(f"Longitud total recorrida: {total_metros:.2f} metros")
    print(f"Longitud total recorrida: {total_yardas:.2f} yardas")
    
except ValueError:
    print("Entrada no válida. Por favor, ingrese un número.")
