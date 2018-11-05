import random
estatua = False
estatua_activada = False
cadaver = False
cofre9 = False
dragon_muerto = False
espada = False
espada_empoderada = False
gemas = False
trampa_activada = False
dragon_persiguiendo = False
seguir_luchando = False
huevo = False
nido= False
vidas = 5
enemigo_vidas = 6

def pregunta_1respuesta(pregunta, respuesta):
    bien_escrito = False
    while bien_escrito == False:
        opcion = input(pregunta)
        if opcion == respuesta:
            print("")
            return opcion
            bien_escrito = True
            
        else:
            print("No entiendo la respuesta, porfavor intentalo de nuevo")
            print("")
            
def pregunta_2respuestas(pregunta, respuesta1, respuesta2):
    bien_escrito = False
    while bien_escrito == False:
        opcion = input(pregunta)
        if opcion == respuesta1 or opcion == respuesta2:
            print("")
            return opcion
            bien_escrito = True
            
        else:
            print("No entiendo la respuesta, porfavor intentalo de nuevo")
            print("")

def pregunta_3respuestas(pregunta, respuesta1, respuesta2, respuesta3):
    bien_escrito = False
    while bien_escrito == False:
        opcion = input(pregunta)
        if opcion == respuesta1 or opcion == respuesta2 or opcion == respuesta3:
            print("")
            return opcion
            bien_escrito = True
            
        else:
            print("No entiendo la respuesta, porfavor intentalo de nuevo")
            print("")
            
def room_title (num):
    print("")
    print("Habitación",num)
    print("------------")    
    pasar_pagina = input()
def quitar_vida (num):
    global vidas
    vidas = vidas -num
    if vidas <= 0:
        print("has muerto")
        game_over()
    else:    
        print("te quedan", vidas, "vidas")   
def combate ():
    global dragon_muerto
    global enemigo_vidas
    global espada_empoderada
    global espada
    global dragon_persiguiendo    
    global seguir_luchando
    escapar = False
    while escapar == False:
        
        
        ataque_dragon = random.randint(1,2)
        if ataque_dragon == 1:
            print("El dragon infla sus pulmones preparandose para descargar sus llamas sobre ti")
            opcion = pregunta_2respuestas("Que quieres hacer, bloquear o esquivar? b/e","b","e")
            if opcion == "b":
                print("Alzas tu escudo para cubrirte")
                pasar_pagina = input()
                print("Aunque el calor de las llamas te quema, tu escudo consigue repeler casi por completo el ataque")
                quitar_vida(1)
                print("")
            else:
                print("Intentas esquivar su ataque")
                pasar_pagina = input()
                print("Pero el alcance de la llamarada es enorme golpenadote casi por completo")
                quitar_vida(2)
                
                print("")
        
        if ataque_dragon == 2:
            print("El dragon alza sus podersoas garras")
            opcion = pregunta_2respuestas("Que quieres hacer, bloquear o esquivar? b/e","b","e")                       
            if opcion == "e":
                print("Intentas esquivar su ataque")
                pasar_pagina = input()
                print("El tamaño del dragon impide que pueda moversa con rapidez")
                print("Por lo que puedes esquivar su ataque con apenas magulladuras")
                quitar_vida(1)
                print("")
            else:
                print("Alzas tu escudo para cubrirte")
                pasar_pagina = input()
                print("Intentas bloquear su ataque pero la devastadora fuerza de la garra te lanza por los aires")
                quitar_vida(2)
                print("")
            
        
        
        opcion = pregunta_2respuestas("contraatacamos? y/n ","y","n")
        if opcion == "y":                
            if espada == False and espada_empoderada == False:
                print ("No haces nada")                        
            elif espada == True and espada_empoderada == True:
                enemigo_vidas = enemigo_vidas - 2
                print("Al enemigo le quedan", enemigo_vidas,"vidas")                    
            elif espada == True or espada_empoderada == True:
                enemigo_vidas = enemigo_vidas - 1
                print("Al enemigo le quedan", enemigo_vidas,"vidas")                     
            if enemigo_vidas<=0:
                print ("has matado al dragon, la bestia no molestara mas")
                print ("")
                escapar = True
                dragon_muerto = True
                dragon_persiguiendo = False
                pasar_pagina = input()
            else:
                opcion = pregunta_2respuestas("Quieres escapar? y/n","y","n")
                if opcion == "y":
                    dragon_persiguiendo = True
                    escapar = True
        elif opcion == "n":
            dragon_persiguiendo = True
            seguir_luchando = True
            escapar = True
                            
def game_over ():
        repetir = pregunta_2respuestas("Queres volver ha jugar? y/n","y","n")
        if repetir == "y":
            game_start()
        if repetir == "n":
            print("hasta la proxima")
    
    
def room9 ():
    global huevo
    global cofre9
    room_title(9)
    
    if cofre9 == False:
        print("Hay un cofre!!")
        opcion = pregunta_2respuestas("Quires abrirlo? y/n","y","n")
        if opcion == "y":
            if huevo == False:
                print("¡El cofre contenia la corona del rey!")
                print("¡Felicidades has salvado el reino!")
                pasar_pagina = input("")
                print("La fama y fortuna te esperan")
                print("Vuelves a casa triunfante de tu mision")
                print("FIN")
                pasar_pagina = input("")
                game_over()
            if huevo == True:
                print("¡El cofre contenia la corona del rey!")
                print("¡Felicidades has salvado el reino!")
                pasar_pagina = input("")
                print("Vuelves a casa, pero ahora con un problema mas")
                print("Que haras con el huevo de dragon? ")
                print("Continuara...")
                pasar_pagina = input("")
                game_over()
                
        else:
            print("Dejas atras el cofre")
    print("En la habitación solo queda una puerta:")
    print("Oeste")
    opcion = pregunta_1respuesta("¿Donde quieres ir? o ","o")
    if opcion == "o":
        room7()
    
def room11 ():
    global huevo
    global nido
    room_title(11)
    print("Este es el nido del dragon")
    if nido == False:
        opcion = pregunta_2respuestas("Quieres investigar? y/n", "y", "n")
        if opcion == "y":
            print("Empiezas a buscar en el nido")
            print("Escondido entre las rocas encuentras un huevo")
            opcion = pregunta_2respuestas("Quieres romper el huevo o te lo quieres quedar? q/r","q","r")
            if opcion =="q":
                print("Te das cuenta que el dragon solo quería proteger su nido")
                print("Sietnes lastima por la cria que esta por nacer y decides quedarte el huevo")
                huevo = True
                nido = True
                pasa_pagina = input("")
            if opcion == "r":
                print("Al ver el huevo te das cuenta del peligro que supone")
                print("Sin pensartelo dos veces rompes el huevo")
                nido = True
                pasa_pagina = input("")
        elif opcion == "n":
            print("Por miedo a lo que puedas encontrar decides no aventurarte mas")
            pasa_pagina = input("")
    print("El nido no tiene salida, por lo que solo puedes volver por donde has venido:")
    print("Sud")
    opcion = pregunta_1respuesta("¿Donde quieres ir? s ","s")
    if opcion == "s":
        room7()
    
def room7 ():
    global dragon_muerto
    room_title(7)
   
    
    if dragon_muerto == False:
        print("Hay un dragon!!!")
        pasar_pagina = input("")
        print("Te pega un leñazo")
        combate ()
        if dragon_muerto == False:
            opcion = pregunta_1respuesta("Solo puedes huir por donde has venido. s ","s")
            if opcion == "s":
                room5()
    if dragon_muerto == True:    
        print("Sin el dragón puedes ver que hay tres puertas")
        print("Este, Sud o Norte ")
        opcion = pregunta_3respuestas("¿Donde quieres ir? e/s/n ","e","s","n")
        if opcion == "e":
            room9()
        elif opcion == "s":
            room5()
        elif opcion == "n":
            room11()
        
def room5 ():
    global dragon_persiguiendo
    room_title(5)
    if dragon_persiguiendo == False:
        print("Es una habitación vacia, pero tiene")
        print("dos puertas:")
        print("Oeste o Norte ")
        opcion = pregunta_2respuestas("¿Donde quieres ir? o/n ","o","n")
        if opcion == "o":
            room4()
        elif opcion == "n":
            room7()
    if dragon_persiguiendo == True:
        print("Has huido de milagro del combate")
        print("Te paras a descansar un poco para recuperarte")
        pasar_pagina = input("")
        print("Escuchas un gran estruendo detras de ti")
        pasar_pagina = input("")
        print("Es el dragón!!!")
        print("Te está persiguiendo!!")
        pasar_pagina = input("")
        print("El dragon a destrozado la puerta y ahora esta delante de ti")
        print("Solo puedes huir")
        print("El dragon tapa la salida del norte")
        opcion = pregunta_1respuesta("La unica salida esta oeste. o","o")
        if opcion == "o":
            room4()
def room6 ():
    global gemas
    global cadaver
    global dragon_persiguiendo
    global dragon_muerto
    
    room_title(6)
    if dragon_persiguiendo == False:
        if cadaver == False:
            print("Parece que en esta habitación ha habido un derrumbamiento, no hay mas salidas")
            print("Te fijas que hay un cadaver sepultado entre los escombros")
            opcion = pregunta_2respuestas("Quires registrar el cadaver? y/n","y","n")
            if opcion == "y":
                print("El cadaver parece de un saqueador")
                print("Entre sus ropas encuentras una bolsa con un par de gemas")
                print("Parecen valiosas y te las guardas")
                print("")
                pasar_pagina = input("")
                gemas = True
                cadaver == True
            else:
                print("Mejor molestar a los muertos")
        if cadaver == True:
            print("Solo hay los escombros y el cadaver")
        print("La habitación esta vacia la unica opción es volver por donde has venido: ")
        print("Sud")
        opcion = pregunta_1respuesta("¿Donde quieres ir? s ","s")
        if opcion == "s":
            room4()
    if dragon_persiguiendo == True:
        print("La habitación no tiene salida")
        print("El dragón entradestryuendo todo a su paso")
        while dragon_muerto == False:
            print("No hay salida, solo queda luchar")
            combat()
        print("Ahora que todo a acabado solo puedes salir por donde has entrado: ")
        print("Sud")
        opcion = pregunta_1respuesta("¿Donde quieres huir? s ","s")
        if opcion == "s":
            room4()
        
def room4 ():
    global dragon_persiguiendo    
    
    room_title(4)
    if dragon_persiguiendo == False: 
        print("Es una habitación vacia, pero tiene tres puertas: ")
        print("Este, Oeste o Norte ")
        opcion = pregunta_3respuestas("¿Donde quieres ir? e/o/n ","e","o","n")
        if opcion == "e":
            room5()
        elif opcion == "o":
            room1()
        elif opcion == "n":
            room6()
    if dragon_persiguiendo == True:
        print("El enrome dragon ha empezado perseguirte, no hay tiempo")
        print("Esta habitación tiene 3 salidas, pero por donde has salido esta el dragon solo quedan 2: ")
        print ("Norte u Oeste")
        opcion = pregunta_2respuestas("¿Por donde quieres huir? n, o", "n","o")
        if opcion == "o":
            room1()
        elif opcion == "n":
            room6()


def room10 ():
    global espada
    global dragon_muerto
    global dragon_persiguiendo
    room_title(10)    
    if espada == False and dragon_persiguiendo == False:
        print("Has encontrado una espada magica!!")
        opcion = pregunta_2respuestas("Quires cogerla? y/n","y","n")
        if opcion == "y":
            print("¡Ahora empuñas la espada magica!")
            print("Aunque algo debil sigues notando que mantiene parte de su poder")
            print("")
            pasar_pagina = input("")
            espada = True
        elif opcion == "n":
            print("Prefieres no jugar con poderes que desconoces")
            print("Dejas atras la espada")
            print("")
            
    if dragon_persiguiendo == False:            
        print("Solo queda una puerta en la habitación, por donde has venido: ")
        print("Norte")
        opcion = pregunta_1respuesta("¿Donde quieres ir? n ","n")
        if opcion == "n":
            room8()
    
    elif dragon_persiguiendo == True and espada == False:
        print("Entras a la camara rapidamente, aún escuachas al dragon")
        print("Vees una espada que parece mágica")
        opcion = pregunta_2respuestas("Quires cogerla? y/n","y","n")
        if opcion == "y":
            print("¡Ahora empuñas la espada magica!")
            print("Aunque algo debil sigues notando que mantiene parte de su poder")
            print("")
            pasar_pagina = input("")
            espada = True
        elif opcion == "n":
            print("Prefieres no jugar con poderes que desconoces")
            print("Dejas atras la espada")
            pasar_pagina = input("")       
        combate()
        
    elif dragon_persiguiendo == True:
        print("El dragón entra en la sala destruyendo todo a su paso")
        pasar_pagina = input("")
        while dragon_muerto == False:
            
            if espada == True:
                print("La salida esta bloqueada, no puedes huir")
                print("Solo puedes luchar")
                pasar_pagina = input("")
                combate()
            if espada == False:
                print("El dragon tapa la salida, no puedes huir")
                print("Pero aun puedes coger la espada magica")
                
                opcion = pregunta_2respuestas("Quires cogerla? y/n","y","n")
                if opcion == "y":
                    print("¡Ahora empuñas la espada magica!")
                    print("Aunque algo debil sigues notando que mantiene parte de su poder")
                    print("")
                    pasar_pagina = input("")
                    espada = True
                    combate()
                elif opcion == "n":
                    print("Prefieres no jugar con poderes que desconoces")
                    print("Sigues luchando con el dragon")
                    pasar_pagina = input("")
                    combate()
    
    
         
        print("Solo queda una puerta en la habitación, por donde has venido: ")
        print("Norte")
        opcion = pregunta_1respuesta("¿Donde quieres ir? n ","n")
        if opcion == "n":
            room8()
            
def room8 ():
    room_title(8)
    global enemigo_vidas
    global dragon_persiguiendo
    global trampa_activada
    global dragon_muerto
    if dragon_persiguiendo == False and trampa_activada ==False: 
        print("Es una gran camara, aun quedan algunos muebles que no han sido destruidos por el tiempo")
        opcion = pregunta_2respuestas("Quieres investigar? y/n", "y", "n")
        if opcion == "y":
            print("")
            print("Encuentras que aun hay una enorme lampara de araña en el techo sostenida por una cuerda")
            opcion2 = pregunta_2respuestas("Quieres cortar la cuerda?y/n", "y", "n")
            if opcion2 == "y":
                print("")
                print ("La lampara cae haciendo un gran destrozo en la sala")
                print ("No queda nada mas en la sala y decides continuar")
                pasar_pagina = input("")
            elif opcion2 == "n":
                print("")
                print("Decides no tocar nada, no sabes lo que podria pasar")
                pasar_pagina = input("")
               
        
        
        print("La habitación tiene dos salidas, por donde has venido y otra: ")
        print("Este o Sur ")
        opcion = pregunta_2respuestas("¿Donde quieres ir? e/s ","e","s")
        if opcion == "e":
            room3()
        elif opcion == "s":
            room10()
    if dragon_persiguiendo == True and trampa_activada == False:
        print("Puedes escuchar como el dragón continua persiguiendote")
        print("La sala es enorme y al medio, sostenida por una cuerda, cuelga una lampara de araña gigante")
               
        opcion = pregunta_2respuestas("Quieres prepararle una trampa al dragon? y/n", "y", "n")
        if opcion == "y":
            trampa_activada = True
            print("El dragon entra en la sala destruyendo todo a su paso")
            print("Esperas a que se acerque lo suficiente")
            print("")
            pasar_pagina = input("")
            print("Finalmente el dragon se alza delante tuyo")
            print("Cortas la cuerda haciendo que la lampara gigante caiga sobre el dragon")
            print("")
            pasar_pagina = input("")
            print("El golpe pilla desprevenida la bestia que empieza a gritar")
            enemigo_vidas = enemigo_vidas - 3
            print("Al enemigo le quedan", enemigo_vidas,"vidas")
            print("Ahora te mira con gran odio y se lanza hacia ti")
            pasar_pagina = input("")
            print("")
            combate()
        elif opcion == "n":
            print("No hay tiempo que perder, debes seguir huiendo")
            print("Solo puedes correr hacia la unica salida que hay al sur")
            pasar_pagina = input("")
            room10()
    
    if dragon_muerto == True:
        print("La habitacón esta destrozada, pero aun puedes ver que quedan dos salidas:")   
        print("Este y Sur ")
        opcion = pregunta_2respuestas("¿Donde quieres ir? e/s ","e","s")
        if opcion == "e":
            room3()
        elif opcion == "s":
            room10()
    if dragon_muerto == False:
        print("No hay tiempo que perder, debes seguir huiendo")
        opcion = pregunta_1respuesta("Solo puedes correr hacia la unica salida que hay al sur. s","s")
        if opcion == "s":
            room10()
        
        
        
        
        
        
def room3 ():
    global estatua
    global estatua_activada
    global espada
    global espada_empoderada
    global dragon_persiguiendo
    room_title(3)
    if dragon_persiguiendo == False:
        if estatua == False:
            print("Hay una estatua en la sala")
            opcion1 = pregunta_2respuestas("Quieres investigar? y/n","y","n")
            if opcion1 == "y" and estatua_activada == False:
                print("Te acercas a la esatua, esta  representa a una antigüa diosa guerrera")
                print("Aunque la habitación esta medio en ruinas la estatua se mantiene en buen estado")
                pasar_pagina = input("")
                print("Al fijarte bien, a la estatua tiene dos hoyos en los ojos")
                pasar_pagina = input("")
                if gemas == True and estatua_activada ==False:             
                    opcion2 = pregunta_2respuestas("Quieres colocar las gemas en los ojos? y/n","y", "n")
                    if opcion2 == "y":
                        print("")
                        print("Las gemas empiezan a resplandecer con un brillo azul")
                        print("La estatua empieza a moverse cambiando su postura, ahora parece quere sostener algo con sus manos")
                        estatua_activada = True
                        pasar_pagina = input("")
                        
                            
                        if espada == True and espada_empoderada == False:
                            opcion3 = pregunta_2respuestas("Quieres poner la espada sobre las manos? y/n","y", "n")
                            if opcion3 == "y":
                                print("La espada empieza a resplandecer con una luz magica, sientes como su poder ha despertado del todo")
                                print("Es hora de seguir")
                                estatua = True
                                espada_empoderada = True
                                pasar_pagina = input("")           
                            elif opcion3 == "n":
                                print("No sabes que clase de criaturas han habitado estas mazmorras ni a que tipo de dioses rendian culto")
                                print("Te apartas de la estatua")
                                pasar_pagina = input("")            
                                            
                        elif espada == False:
                            print("No sabes muy bien que hacer con la estatus asi que te apartas y sigues con tu aventura")
                            pasar_pagina = input("")
                    elif opcion2 == "n":
                        print("Las gemas parecen tener un precio muy alto, te las guardas y sigues con tu aventura")
                        pasar_pagina = input("")
                elif gemas == False:
                    print("No observas nada mas especial")
                    pasar_pagina = input("")
                
                
            elif  opcion1 == "y" and estatua_activada == True:
                print("La estatua sigue como la dejaste, con los ojos brillando y esperando")
                if espada == True and espada_empoderada == False:
                    opcion3 = pregunta_2respuestas("Quieres poner la espada sobre las manos? y/n","y", "n")
                    if opcion3 == "y":
                        print("La espada empieza a resplandecer con una luz magica, sientes como su poder ha despertado del todo")
                        print("Es hora de seguir")
                        estatua = True
                        espada_empoderada = True
                        pasar_pagina = input("")                   
                    elif opcion3 == "n":
                        print("")
                        print("No sabes que classe de criaturas han habitado estas mazmorras ni a que tipo de dioses rendian culto")
                        print("Te apartas de la estatua")
                        pasar_pagina = input("")
                elif espada == False:
                    print("No sabes muy bien que hacer con la estatus asi que te apartas i sigues con tu aventura")
                    pasar_pagina = input("")
            
            elif opcion1 == "n":
                print("Prefieres no jugar con deidades desconocidas")
                pasar_pagina = input("")
            
       
                 
        print("En la habitación aun se puede ver la estatua")
        print("Para poder salir hay dos puertas: ")
        print("Sur o Oeste ")
        opcion = pregunta_2respuestas("¿Donde quieres ir? s/o ","s","o")
        if opcion == "o":
            room8()
        elif opcion == "s":
            room2()
    elif dragon_persiguiendo== True:
        print("Escuchas el dragón como te persigue")
        print("No tienes tiempo para investigar la sala")
        pasar_pagina = input("")
        opcion = pregunta_1respuesta("La habitación solo tiene una salida al oeste por donde puedes huir o: o ","o")
        if opcion == "o":
            room8()
        
def room2 ():
    global dragon_persiguiendo
    
    room_title(2)
    
    if dragon_persiguiendo == False:
        print("Es una habitación vacia, pero tiene dos puertas: ")
        print("Norte o Este ")
        opcion = pregunta_2respuestas("¿Donde quieres ir?n/e ", "n", "e")
        if opcion == "e":
            room1()
        elif opcion == "n":
            room3()
    elif dragon_persiguiendo == True:
        print("Escuchas como el dragón destroza todo por donde pasa, esta cada vez mas cerca")
        
        pasar_pagina = input("")
        opcion = pregunta_1respuesta("La habitación solo tiene una salida al norte por donde puedes huir: n ","n")
        if opcion == "n":
            room3()
      
def room1 ():
    room_title(1)
    if dragon_persiguiendo == False:
        print("Te encuentras a la entrada de la mazmorra")
        print("Aunque la mayor parte de esta habitación ha sido devorada por la naturaleza aún puedes distinguir lo que antes eran dos puertas:")
        print("Una al este y otra al oeste")
        opcion = pregunta_2respuestas("¿Donde quieres ir?e/o ","e","o")
        if opcion == "e":
            room4()
        elif opcion == "o":
            room2()
    if dragon_persiguiendo == True:
        print("Estas en la entrada de la mazmorra y escuchas como el dragón esta cada vez mas cerca")
        print("Puedes ver la salida de la mazmorra y otra puerta al oeste")
        opcion = pregunta_2respuestas("Quieres huir de la mazmorra o ir por la puerta del ose mas? o/h","h","o")
        if opcion == "h":
            print("Huyes de la mazmorra como un cobarde")
            print("Has perdido")
            game_over()
        if opcion == "o":
            print("Huir no es una opcion, solo queda seguir al oeste")            
            room2()

def game_start():
    print("!Bienvenido a Creepy Dungeon")
    print("----------------------------")
    print("Delante tuyo tienes una mazmorra")    
    respuesta = pregunta_2respuestas("¿Quieres entrar? Sí(y) o No (n)", "y", "n")    
    if respuesta == "y":
        print("Empieza el juego")       
        room1()
    elif respuesta == "n":
        print("Eres un cagueta")


game_start()


