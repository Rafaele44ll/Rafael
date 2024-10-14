import os
os.system("cls")

votos_pamela = int(input("Ingrese los votos de Pamela: "))
votos_carol = int(input("Ingrese los votos de Carol: "))
votos_fanny = int(input("Ingrese los votos de Fanny: "))

total_votos = votos_pamela + votos_carol + votos_fanny

votos_necesarios = (total_votos // 2) + 1

if votos_pamela >= votos_necesarios:
    print("La ganadora es: Pamela")
elif votos_carol >= votos_necesarios:
    print("La ganadora es: Carol")
elif votos_fanny >= votos_necesarios:
    print("La ganadora es: Fanny")
else:
    
    if (votos_pamela == votos_carol == votos_fanny):
        print("La elección se anula por empate.")
    elif (votos_pamela == votos_carol) or (votos_carol == votos_fanny) or (votos_fanny == votos_pamela):
        print("La elección se anula por empate en el segundo puesto.")
    else:
        
        if votos_pamela > votos_carol and votos_pamela > votos_fanny:
            print("1° puesto: Pamela")
            if votos_carol > votos_fanny:
                print("2° puesto: Carol")
                print("3° puesto: Fanny")
            else:
                print("2° puesto: Fanny")
                print("3° puesto: Carol")
        elif votos_carol > votos_pamela and votos_carol > votos_fanny:
            print("1° puesto: Carol")
            if votos_pamela > votos_fanny:
                print("2° puesto: Pamela")
                print("3° puesto: Fanny")
            else:
                print("2° puesto: Fanny")
                print("3° puesto: Pamela")
        else:
            print("1° puesto: Fanny")
            if votos_pamela > votos_carol:
                print("2° puesto: Pamela")
                print("3° puesto: Carol")
            else:
                print("2° puesto: Carol")
                print("3° puesto: Pamela")
