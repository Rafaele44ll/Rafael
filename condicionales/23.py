import os
os.system("cls")

nota_matematicas = int(input("Ingrese la nota de Matemáticas (0-20): "))
nota_fisica = int(input("Ingrese la nota de Física (0-20): "))

if nota_matematicas > 17:
    propina_matematicas = 3  
else:
    propina_matematicas = nota_matematicas  

if nota_fisica > 15:
    propina_fisica = 2  
else:
    propina_fisica = 0  

total_propina = propina_matematicas + propina_fisica

promedio = (nota_matematicas + nota_fisica) // 2  

print(f"Propina de Matemáticas: S/. {propina_matematicas}")
print(f"Propina de Física: S/. {propina_fisica}")
print(f"Total de propina: S/. {total_propina}")

if promedio > 16:
    print("¡El padre obsequiará un reloj!")
