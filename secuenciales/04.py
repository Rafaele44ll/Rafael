import os
os.system("cls")

def convertir_a_metros(pies, pulgadas):

    metros_pies = pies * 0.3048  # 1 pie = 0.3048 metros
    
    metros_pulgadas = pulgadas * 0.0254  # 1 pulgada = 0.0254 metros
    
    total_metros = metros_pies + metros_pulgadas
    return total_metros

try:
    estatura_ingresa = input("Ingrese su estatura en formato inglés (X' Y''): ")
    
    partes = estatura_ingresa.split("'")
    pies = int(partes[0].strip())  
    pulgadas = int(partes[1].strip().replace('"', ''))  
    
    estatura_metros = convertir_a_metros(pies, pulgadas)
    
    print(f"Su estatura en metros es: {estatura_metros:.2f} m")
    
except (ValueError, IndexError):
    print("Entrada no válida. Por favor, ingrese la estatura en el formato correcto (X' Y'').")
