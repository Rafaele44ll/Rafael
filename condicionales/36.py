import os
os.system("cls")

cuadernos = int(input("Ingrese el número de cuadernos adquiridos: "))

lapiceros_lucas = 0
lapiceros_faber = 0
lapiceros_pilot = 0

lapiceros_lucas += (cuadernos // 4) * (1 if cuadernos >= 12 and cuadernos < 24 else 0)
lapiceros_faber += (cuadernos // 4) * (2 if cuadernos >= 24 and cuadernos < 36 else 0)
lapiceros_pilot += (cuadernos // 4) * (2 if cuadernos >= 36 else 0)
lapiceros_faber += (cuadernos // 6) * (1 if cuadernos >= 36 else 0)
lapiceros_lucas += (cuadernos // 12) * (1 if cuadernos >= 36 else 0)

print("Lapiceros Lucas obsequiados:", lapiceros_lucas)
print("Lapiceros Faber obsequiados:", lapiceros_faber)
print("Lapiceros Pilot obsequiados:", lapiceros_pilot)
