def convertir_a_metros(pies, pulgadas):
    # Conversión de pies a metros
    metros_pies = pies * 0.3048  # 1 pie = 0.3048 metros
    
    # Conversión de pulgadas a metros
    metros_pulgadas = pulgadas * 0.0254  # 1 pulgada = 0.0254 metros
    
    # Suma total en metros
    total_metros = metros_pies + metros_pulgadas
    return total_metros

try:
    # Entrada del usuario en formato "X' Y''"
    estatura_ingresa = input("Ingrese su estatura en formato inglés (X' Y''): ")
    
    # Procesar la entrada para extraer pies y pulgadas
    partes = estatura_ingresa.split("'")
    pies = int(partes[0].strip())  # Parte antes de la comilla simple
    pulgadas = int(partes[1].strip().replace('"', ''))  # Parte después de la comilla simple y quitar comillas dobles
    
    # Cálculo de la estatura total en metros
    estatura_metros = convertir_a_metros(pies, pulgadas)
    
    # Resultado
    print(f"Su estatura en metros es: {estatura_metros:.2f} m")
    
except (ValueError, IndexError):
    print("Entrada no válida. Por favor, ingrese la estatura en el formato correcto (X' Y'').")
