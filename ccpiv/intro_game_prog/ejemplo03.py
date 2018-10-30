import random

numero = random.randint(1,50)
continuar = True
while continuar:
    jugador = int(input("Introduce un numero: "))
    if jugador < numero:
        print("Es mayor")
    elif jugador > numero:
        print("Es menor")
    else:
        print("Has acertado!")
        continuar = False