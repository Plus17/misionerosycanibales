#!usr/bin/python

#Python 2.7.x

orillaorigen ={'misioneros': 3, 'canibales': 3}
balsa = {'misioneros': 0 , 'canibales' : 0}
orilladestino ={'misioneros': 0, 'canibales': 0}


def validaorillaorigen():
	if orillaorigen['misioneros'] < orillaorigen['canibales']:
		print "Los canibales son mas que los misioneros"
		print "M: %s C: %s  ~~~~~~~~~~ M: %s C: %s \n" % (orillaorigen['misioneros'], orillaorigen['canibales'], orilladestino['misioneros'],orilladestino['canibales'] )
		return False
	else:
		return True

def validaorilladestino():
	if orilladestino['misioneros'] < orilladestino['canibales']:
		print "Los canibales son mas que los misioneros"
		print "M: %s C: %s  ~~~~~~~~~~ M: %s C: %s \n" % (orillaorigen['misioneros'], orillaorigen['canibales'], orilladestino['misioneros'],orilladestino['canibales']  )
		return False
	else:
		return True

def validarentrada(letra):
	# si la letra es M se agrega un misionero a la balsa y se resta uno a la orilla de origen
	if letra == 'M': 
		return letra
	# si la letra es C se agrega un canibal a la balsa y se resta uno a la orilla de origen
	elif letra == 'C':
		return letra
	# si la letra nos ni M ni C termina el script
	else:
		print "Entrada invalida"
		return False
		
def subirbalsa():
	letra1 = str(raw_input("Precione M para subir un misionero o C para subir a un canibal \n"))
	letra1 = letra1.upper()
	letra1 = validarentrada(letra1)
	return letra1

def bajarbalsa():
	bajam = str(raw_input("Preciona M para bajar misionero o C para bajar un canibal \n"))
	bajam = bajam.upper()
	bajam = validarentrada(bajam)
	return bajam

def subir(donde):
	if donde == 'origen':
	 	letra = subirbalsa()

		if letra == 'M':
			if orillaorigen['misioneros'] ==0:
				print "No hay misioneros para subir \n"
			elif balsa['misioneros'] + balsa['canibales'] >= 2:
				print "Ya no caben en la balsa \n"
			else:	
				balsa['misioneros'] += 1
				orillaorigen['misioneros'] -=1

		elif letra == 'C':
			if orillaorigen['canibales'] ==0:
				print "No hay canibales para subir \n"
			elif balsa['misioneros'] + balsa['canibales'] >= 2:
				print "Ya no caben en la balsa \n"
			else:	
				balsa['canibales'] += 1
				orillaorigen['canibales'] -= 1


		letra2 = subirbalsa()

		if letra2 == 'M':
			if orillaorigen['misioneros'] ==0:
				print "No hay misioneros para subir \n"
			elif balsa['misioneros'] + balsa['canibales'] >= 2:
				print "Ya no caben en la balsa \n"
			else:	
				balsa['misioneros'] += 1
				orillaorigen['misioneros'] -=1
		elif letra2 == 'C':
			if orillaorigen['canibales'] ==0:
				print "No hay canibales para subir \n"
			elif balsa['misioneros'] + balsa['canibales'] >= 2:
				print "Ya no caben en la balsa \n"
			else:	
				balsa['canibales'] += 1
				orillaorigen['canibales'] -= 1
				

	elif donde == 'destino':
		letra = subirbalsa()

		if letra == 'M':
			if orilladestino['misioneros'] ==0:
				print "No hay misioneros para subir \n"
			elif balsa['misioneros'] + balsa['canibales'] >= 2:
				print "Ya no caben en la balsa \n"
			else:	
				balsa['misioneros'] += 1
				orilladestino['misioneros'] -=1
		elif letra == 'C':
			if orilladestino['canibales'] ==0:
				print "No hay canibales para subir \n"
			elif balsa['misioneros'] + balsa['canibales'] >= 2:
				print "Ya no caben en la balsa \n"
			else:	
				balsa['canibales'] += 1
				orilladestino['canibales'] -= 1



		letra2 = subirbalsa()

		if letra2 == 'M':
			if orilladestino['misioneros'] ==0:
				print "No hay misioneros para subir \n"
			elif balsa['misioneros'] + balsa['canibales'] >= 2:
				print "Ya no caben en la balsa \n"
			else:	
				balsa['misioneros'] += 1
				orilladestino['misioneros'] -=1
		elif letra2 == 'C':
			if orilladestino['canibales'] ==0:
				print "No hay canibales para subir \n"
			elif balsa['misioneros'] + balsa['canibales'] >= 2:
				print "Ya no caben en la balsa \n"
			else:	
				balsa['canibales'] += 1
				orilladestino['canibales'] -= 1


def bajar(donde):
	if donde == 'origen':
		count = balsa['misioneros']
		count2 = balsa['canibales']
		while count > 0:
			opcionbajar = input("Bajar al misionero? 1: Si 2: No \n")
			if opcionbajar  == 1:
				balsa['misioneros'] -=1
				orillaorigen['misioneros'] += 1
				count -= 1
			elif opcionbajar  == 2:
				count -=1
		

		while count2 > 0:
			opcionbajar = input("Bajar al canibal? 1: Si 2: No \n")
			if opcionbajar  == 1:
				balsa['canibales'] -=1
				orillaorigen['canibales'] += 1
				count2 -= 1
			elif opcionbajar  == 2:
				count2 -=1
			if validaorillaorigen() == False:
				break


	elif donde == 'destino':
		count = balsa['misioneros']
		count2 = balsa['canibales']
		while count > 0:
			opcionbajar = input("Bajar al misionero? 1: Si 2: No \n")
			if opcionbajar  == 1:
				balsa['misioneros'] -=1
				orilladestino['misioneros'] += 1
				count -= 1
			elif opcionbajar  == 2:
				count -=1


		while count2 > 0:
			opcionbajar = input("Bajar al canibal? 1: Si 2: No \n")
			if opcionbajar  == 1:
				balsa['canibales'] -=1
				orilladestino['canibales'] += 1
				count2 -= 1
			elif opcionbajar  == 2:
				count2 -=1

def main():
	turno = 1
	estado = True
	remar = 0
	while (estado == True):

		print "M: %s C: %s ~~~~~~~~~~   M: %s C: %s \n" % (orillaorigen['misioneros'], orillaorigen['canibales'], orilladestino['misioneros'], orilladestino['canibales']  )
		subir('origen')
		remar = input("1: Remar \n")
		if remar == 1:
			print "M: %s C: %s ~~~~~~~~~~   M: %s C: %s \n" % (orillaorigen['misioneros'], orillaorigen['canibales'], orilladestino['misioneros'], orilladestino['canibales']  )
			print "Balsa: misioneros: %s canibales: %s" % (balsa['misioneros'], balsa['canibales'])
			if validaorillaorigen() == False:
				break
			else:
				bajar('destino')
				remar = input("1: Remar de regreso 2: Subir \n")
			if remar == 1:
				if balsa['misioneros'] + balsa['canibales'] > 0:
					print "M: %s C: %s ~~~~~~~~~~ M: %s C: %s \n" % (orillaorigen['misioneros'], orillaorigen['canibales'], orilladestino['misioneros'],orilladestino['canibales']  )
					print "Balsa: misioneros: %s canibales: %s" % (balsa['misioneros'], balsa['canibales'])
					if validaorilladestino() == False:
						break
					
				else:
					print "debe haber un misionero o canibal para remar \nr"
					subir('destino')
					remar == 1
			elif remar ==2:
				subir('destino')
				if balsa['misioneros'] + balsa['canibales'] > 0:
					print "M: %s C: %s  ~~~~~~~~~~ M: %s C: %s \n" % (orillaorigen['misioneros'], orillaorigen['canibales'], orilladestino['misioneros'],orilladestino['canibales']   )
					print "Balsa: misioneros: %s canibales: %s" % (balsa['misioneros'], balsa['canibales'])
					if validaorilladestino() == False:
						break
					
				else:
					print "debe haber un misionero o canibal para remar \n"
					subir('destino')
		else: 
			print "Entrada invalida"
		turno += 1

	print "Utilizo %i turnos \n" % (turno)




if __name__ == "__main__":
	print "M: 3 C: 3 \____/ ~~~~~~~~~~ M: 0 C: 0 "
	main()
