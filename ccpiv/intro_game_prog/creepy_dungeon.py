cofre3 = False
cofre6 = False
cofre9 = False

espada = False
brazalete = False

vidas = 3
enemigo_vidas = 4

def game_over ():
    print("HAS MUERTO")

def room_title (num):
    print("")
    print("Habitación",num)
    print("------------")

def room11 ():
    room_title(11)
    print("¡No hay nada!")
    print("Sólo hay una puertas:")
    print("Sur")
    opcion = input("¿Dónde quieres ir? (s) ")
    if opcion == "s":
        room7()
        
def room10 ():
    room_title(10)
    print("¡Hay una espada!")
    print("Y una puerta:")
    print("Norte")
    opcion = input("¿Dónde quieres ir? (n) ")
    if opcion == "n":
        room8()
        
def room9 ():
    print("Habitación 9")
    print("------------")
    print("¡Hay cofre!")
    print("Y una puerta:")
    print("Oeste")
    opcion = input("¿Dónde quieres ir? (o) ")
    if opcion == "o":
        room7()
 
def room8 ():
    print("Habitación 8")
    print("------------")
    print("¡No hay nada!")
    print("Sólo hay dos puertas:")
    print("Este o Sur")
    opcion = input("¿Dónde quieres ir? (e/s) ")
    if opcion == "e":
        room3()
    elif opcion == "s":
        room10()



        
def room7 ():
    global espada
    global brazalete
    global enemigo_vidas
    global vidas
    
    room_title(7)
    
    print("¡HAY UN MALO MALOSO!")
    print("Te mete un leñazo")
    vidas = vidas - 1
    print("Te quedan", vidas)
    opcion = input("¿Contraatacamos? (y/n) ")
    if opcion == "y":
        escapar = False
        while escapar == False:
            if espada == False and brazalete == False:
                print("No haces nada")
            elif espada == True and brazalete == True:
                enemigo_vidas = enemigo_vidas - 2
                print("Al enemigo le quedan", enemigo_vidas, "vidas")
            elif espada == True or brazalete == True:
                enemigo_vidas = enemigo_vidas - 1
                print("Al enemigo le quedan", enemigo_vidas, "vidas")
            
            if enemigo_vidas <= 0:
                print("Has matado al enemigo")
            else:
                opcion = input("¿Quieres escapar? (y/n)")
                if opcion == "y":
                    escapar = True
                else:
                    vidas = vidas - 1
                    print("Te quedan", vidas)
                    if vidas <= 0:
                        game_over()
    
    
    print("Tres puertas:")
    print("Norte, Este y Sur")
    opcion = input("¿Dónde quieres ir? (n/e/s) ")
    if opcion == "e":
        room9()
    elif opcion == "n":
        room11()
    elif opcion == "s":
        room5()

def room6 ():
    print("Habitación 6")
    print("------------")
    print("¡Hay cofre!")
    print("Y una puerta:")
    print("Sur")
    opcion = input("¿Dónde quieres ir? (s) ")
    if opcion == "s":
        room4()
 



def room5 ():
    print("Habitación 5")
    print("------------")
    print("Es una habitación vacía, pero tiene")
    print("Dos puertas:")
    print("Oeste y Norte")
    opcion = input("¿Dónde quieres ir? (o/n) ")
    if opcion == "o":
        room4()
    elif opcion == "n":
        room7()


def room4 ():
    print("Habitación 4")
    print("------------")
    print("Es una habitación vacía, pero tiene")
    print("tres puertas:")
    print("Oeste, Este y Norte")
    opcion = input("¿Dónde quieres ir? (o/e/n) ")
    if opcion == "e":
        room5()
    elif opcion == "o":
        room1()
    elif opcion == "n":
        room6()

def room3 ():
    global cofre3
    
    room_title(3)
    
    if cofre3 == False:
        print("¡Hay cofre!")
        opcion = input("¿Quieres abrirlo? (y/n) ")
        if opcion == "y":
            print("¡Había una moneda!")
            cofre3 = True
    
    print("Y dos puertas:")
    print("Oeste o Sur")
    opcion = input("¿Dónde quieres ir? (o/s) ")
    if opcion == "o":
        room8()
    elif opcion == "s":
        room2()

def room2 ():
    room_title(2)
    print("Es una habitación vacía, pero tiene")
    print("dos puertas:")
    print("Norte o Este")
    opcion = input("¿Dónde quieres ir? (n/e) ")
    if opcion == "n":
        room3()
    elif opcion == "e":
        room1()

def room1 ():
    room_title(1)
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
    
    
#game_start()
room7()