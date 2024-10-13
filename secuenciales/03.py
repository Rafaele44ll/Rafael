def convertir_a_metros(kilometros, pies, millas):
    # Conversión de kilómetros a metros
    metros_kilometros = kilometros * 1000
    
    # Conversión de pies a metros
    metros_pies = pies / 3.2808
    
    # Conversión de millas a metros
    metros_millas = millas * 1609
    
    # Longitud total en metros
    total_metros = metros_kilometros + metros_pies + metros_millas
    
    return total_metros

def metros_a_yardas(metros):
    return metros / 0.9144  # 1 yarda = 0.9144 metros

try:
    # Entradas del usuario
    kilometros = float(input("Ingrese la longitud del primer tramo en kilómetros: "))
    pies = float(input("Ingrese la longitud del segundo tramo en pies: "))
    millas = float(input("Ingrese la longitud del tercer tramo en millas: "))
    
    # Cálculo de la longitud total en metros
    total_metros = convertir_a_metros(kilometros, pies, millas)
    
    # Conversión a yardas
    total_yardas = metros_a_yardas(total_metros)
    
    # Resultados
    print(f"Longitud total recorrida: {total_metros:.2f} metros")
    print(f"Longitud total recorrida: {total_yardas:.2f} yardas")
    
except ValueError:
    print("Entrada no válida. Por favor, ingrese un número.")
