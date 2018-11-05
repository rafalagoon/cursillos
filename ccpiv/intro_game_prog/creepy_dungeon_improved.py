import sys

cofre3 = False
cofre6 = False
cofre9 = False

espada = False
brazalete = False
corona = False

vidas = 3
enemigo_vidas = 4

def showGameOver ():
	print("")
	print("+-+-+-+-+-")
	print("HAS MUERTO")
	print("+-+-+-+-+-")

def room_title (num):
	print("")
	print("Habitación", num)
	print("-------------")

def enemigo ():
	global espada
	global brazalete
	global enemigo_vidas
	global vidas

	print("¡HAY UN MALO MALOSO!")
	print("Te mete un leñazo")
	vidas = vidas - 1

	print("Te quedan", vidas, "vidas")
	
	while True:
		opcion = input("¿Contraatacamos? (y/n) ")
		if opcion == "n":
			return

		print("Pegas al enemigo")

		if not espada and not brazalete:
			print("Pegas con la mano blanda.")
			print("No haces nada.")
			print("Al enemigo le quedan", enemigo_vidas, "vidas")

		elif espada and brazalete:
			print("Tienes la espada y el brazalete, haces 2 de daño.")
			enemigo_vidas = enemigo_vidas - 2
			print("Al enemigo le quedan", enemigo_vidas, "vidas")

		elif espada or brazalete:
			if espada:
				print("Tienes la espada, haces 1 de daño.")
			else:
				print("Tienes el brazalete, haces 1 de daño.")
			enemigo_vidas = enemigo_vidas - 1
			print("Al enemigo le quedan", enemigo_vidas, "vidas")
			
		if enemigo_vidas <= 0:
			print("¡Has matado al enemigo!")
			print("Puedes continuar")
			return
		else:
			opcion = input("¿Quieres escapar? (y/n)")
			if opcion == "y":
				return
			else:
				print("Te mete otro leñazo")
				vidas = vidas - 1
				print("Te quedan", vidas, "vidas")
				if vidas <= 0:
					showGameOver()
					sys.exit()


def room11 ():
	room_title(11)
	print("¡No hay nada!")
	print("Sólo hay una puerta: Sur")
	while True:
		opcion = input("¿Dónde quieres ir? (s) ")
		if opcion == "s":
			return 7
		else:
			print("Opción errónea")
		
def room10 ():
	global espada

	room_title(10)

	if not espada:
		print("¡Hay una espada!")
		opcion = input("¿Quieres cogerla? (y/n) ")
		if opcion == "y":
			print("¡CONSIGUES LA ESPADA DEL PODER!")
			espada = True

	print("Hay una puerta: Norte")
	while True:
		opcion = input("¿Dónde quieres ir? (n) ")
		if opcion == "n":
			return 8
		else:
			print("Opción errónea")
		
def room9 ():
	global cofre9
	global corona

	room_title(9)

	if not cofre9:
		print("¡Hay cofre!")
		opcion = input("¿Quieres abrirlo? (y/n) ")
		if opcion == "y":
			print("¡¡¡HAS ENCONTRADO LA CORONA!!!")
			print("¡Sal corriendo de la mazmorra!")
			cofre9 = True
			corona = True

	print("Hay puerta: Oeste")
	while True:
		opcion = input("¿Dónde quieres ir? (o) ")
		if opcion == "o":
			return 7
		else:
			print("Opción errónea")
 
def room8 ():
	room_title(8)
	print("¡No hay nada!")
	print("Sólo hay dos puertas: Este o Sur")
	while True:
		opcion = input("¿Dónde quieres ir? (e/s) ")
		if opcion == "e":
			return 3
		elif opcion == "s":
			return 10
		else:
			print("Opción errónea")
		
def room7 ():
	global enemigo_vidas
	
	room_title(7)
	
	if enemigo_vidas > 0:
		enemigo()

	if enemigo_vidas > 0:
		print("Una puerta: Sur")
		while True:
			opcion = input("¿Dónde quieres ir? (s) ")
			if opcion == "s":
				return 5
			else:
				print("Opción errónea")
	else:
		print("Tres puertas: Norte, Este y Sur")
		while True:
			opcion = input("¿Dónde quieres ir? (n/e/s) ")
			if opcion == "e":
				return 9
			elif opcion == "n":
				return 11
			elif opcion == "s":
				return 5
			else:
				print("Opción errónea")
	

def room6 ():
	global cofre6
	global brazalete

	room_title(6)

	if not cofre6:
		print("¡Hay cofre!")
		opcion = input("¿Quieres abrirlo? (y/n) ")
		if opcion == "y":
			print("¡¡HAS ENCONTRADO EL BRAZALETE DE LOS RELÁMPAGOS!!")
			cofre6 = True
			brazalete = True

	print("Y una puerta: Sur")
	while True:
		opcion = input("¿Dónde quieres ir? (s) ")
		if opcion == "s":
			return 4
		else:
			print("Opción errónea")


def room5 ():
	room_title(5)

	print("Es una habitación vacía, pero tiene")
	print("Dos puertas: Oeste y Norte")
	while True:
		opcion = input("¿Dónde quieres ir? (o/n) ")
		if opcion == "o":
			return 4
		elif opcion == "n":
			return 7
		else:
			print("Opción errónea")
		

def room4 ():
	room_title(4)
	print("Es una habitación vacía, pero tiene")
	print("Tres puertas: Oeste, Este y Norte")
	while True:
		opcion = input("¿Dónde quieres ir? (o/e/n) ")
		if opcion == "e":
			return 5
		elif opcion == "o":
			return 1
		elif opcion == "n":
			return 6
		else:
			print("Opción errónea")

def room3 ():
	global cofre3
	
	room_title(3)
	
	if not cofre3:
		print("¡Hay cofre!")
		opcion = input("¿Quieres abrirlo? (y/n) ")
		if opcion == "y":
			print("¡Había una moneda!")
			cofre3 = True
	
	print("Y dos puertas: Oeste o Sur")
	while True:
		opcion = input("¿Dónde quieres ir? (o/s) ")
		if opcion == "o":
			return 8
		elif opcion == "s":
			return 2
		else:
			print("Opción errónea")

def room2 ():
	room_title(2)
	print("Es una habitación vacía, pero tiene")
	print("Dos puertas: Norte o Este")
	while True:
		opcion = input("¿Dónde quieres ir? (n/e) ")
		if opcion == "n":
			return 3
		elif opcion == "e":
			return 1
		else:
			print("Opción errónea")

def room1 ():
	room_title(1)
	if corona == True:
		print("¡HAS SALIDO VIVO Y CON LA CORONA!")
		print("¡HAS GANADO!")
		return 999

	print("Es una habitación vacía, pero tiene")
	print("Dos puertas: Este u Oeste")
	while True:
		opcion = input("¿Dónde quieres ir? (e/o) ")
		if opcion == "e":
			return 4
		elif opcion == "o":
			return 2
		else:
			print("Opción errónea")

def game_start ():
	print("")
	print("¡Bienvenido a Creepy Dungeon!")
	print("-----------------------------")
	print("Delante tuyo tienes una mazmorra")
	print("¿Quieres entrar?")
	respuesta = input("SÍ (y) o NO (n): ")
	
	if respuesta == "n":
		print("Eres un cagueta")
		sys.exit()

	print("")
	print("¡¡¡Empieza el juego!!!")
	print("")

	return 1

	
	
if __name__ == "__main__":
	room_cur = game_start()

	game_over = False

	while not game_over:
		if room_cur == 1:
			room_cur = room1()
		elif room_cur == 2:
			room_cur = room2()
		elif room_cur == 3:
			room_cur = room3()
		elif room_cur == 4:
			room_cur = room4()
		elif room_cur == 5:
			room_cur = room5()
		elif room_cur == 6:
			room_cur = room6()
		elif room_cur == 7:
			room_cur = room7()
		elif room_cur == 8:
			room_cur = room8()
		elif room_cur == 9:
			room_cur = room9()
		elif room_cur == 10:
			room_cur = room10()
		elif room_cur == 11:
			room_cur = room11()
		elif room_cur == 999:
			game_over = True


