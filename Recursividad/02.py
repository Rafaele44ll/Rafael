import os
os.system("cls")

import os
os.system("cls")

def mcd(a, b):
    if b == 0:
        return a
    return mcd(b, a % b)

resultado = mcd(48, 18)
print(resultado)  