import os
os.system("cls")

capacidad_gb = int(input("Ingrese la capacidad del disco duro en gigabytes: "))

capacidad_mb = capacidad_gb * 1024                
capacidad_kb = capacidad_mb * 1024                 
capacidad_bytes = capacidad_kb * 1024             

print(f"Capacidad en megabytes: {capacidad_mb} MB")
print(f"Capacidad en kilobytes: {capacidad_kb} KB")
print(f"Capacidad en bytes: {capacidad_bytes} bytes")


