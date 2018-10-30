def room2 ():
    print("Habitación 2")
    print("------------")
    print("Es una habitación vacía, pero tiene")
    print("dos puertas:")
    print("Norte o Este")
    opcion = input("¿Dónde quieres ir? (n/e) ")
    if opcion == "n":
        room3()
    elif opcion == "e":
        room1()



def room1 ():
    print("Habitación 1")
    print("------------")
    print("Es una habitación vacía, pero tiene")
    print("dos puertas:")
    print("Este u Oeste")
    opcion = input("¿Dónde quieres ir? (e/o) ")
    if opcion == "e":
        room4()
    elif opcion == "o":
        room2()

def game_start ():
    print("¡Bienvenido a Creepy Dungeon!")
    print("-----------------------------")
    print("Delante tuyo tienes una mazmorra")
    print("¿Quieres entrar?")
    respuesta = input("SÍ (y) o NO (n): ")
    
    if respuesta == "y":
        print("Empieza el juego")
        print("")
        room1()
    else:
        print("Eres un cagueta")
    
    
game_start()