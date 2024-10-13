import os
os.system("cls")

def convertir_disco_duro(capacidad_gb):
    capacidad_mb = capacidad_gb * 1024
    capacidad_kb = capacidad_mb * 1024
    capacidad_bytes = capacidad_kb * 1024
    
    return capacidad_mb, capacidad_kb, capacidad_bytes

try:
    capacidad_gb = float(input("Ingrese la capacidad del disco duro en gigabytes: "))
    
    (capacidad_gb < 0) and (_ for _ in ()).throw(ValueError("La capacidad no puede ser negativa."))
    
    capacidad_mb, capacidad_kb, capacidad_bytes = convertir_disco_duro(capacidad_gb)
    
    print(f"Capacidad en megabytes: {capacidad_mb:.2f} MB")
    print(f"Capacidad en kilobytes: {capacidad_kb:.2f} KB")
    print(f"Capacidad en bytes: {capacidad_bytes:.2f} Bytes")

except ValueError as e:
    print(f"Entrada no válida: {e}")

