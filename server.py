import socket
import RPi.GPIO as GPIO
import time ## Import 'time' library. Allows us to use 'sleep'
import command
import os
import signal
import capteur
import moteurs
import configgpio

#-------------------------GPIO_BOARD_CONFIG---------------------------------
#GPIO.setmode(GPIO.BOARD) ## Use board pin numbering
#GPIO.setup(7, GPIO.OUT) ## Setup GPIO Pin 7 to OUT
#===========================================================================

#-------------------------TCP_SERVER_CONFIG---------------------------------
#adresse du raspberry et port sur lequel l'appli va se connecter
HOST = '192.168.42.1'
PORT = 2155
BUFFER_SIZE = 2048
#===========================================================================

#------------------------Initialization_Server------------------------------
# creation du socket 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1) #Maximum 1 host connected to the sock
#===========================================================================

#socket prevu pour les reponses
r = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
r.bind((HOST,2156))
r.listen(1)



#--------------------Inialisation des capteurs ---------------------------
capteur1 = capteur.Capteur(28, 30)
#capteur2 = capteur.Capteur(29, 31)
detected = False
tryDetect1 = True
#tryDetect2 = True
#==========================================================================


#-------------------------signals-----------------------------------------
# fonction pour l'envoi des signaux NON RETENU
#def fonctionsignal(a,b):
#	print('signal recu')
#	
#signal.signal(signal.SIGUSR1,fonctionsignal)
#========================================================================


#connexion
conn, addr = s.accept()
#connr, addrr = r.accept()
#print 'Connection address:", addr
while 1:
	configgpio.cleangpios()
	configgpio.setgpios()

	print ">"

	try:	
		data = conn.recv(BUFFER_SIZE)
	except KeyboardInterrupt:
		conn.close()


#	if not data: break
	print "received data:", data

	print "mesure ultrasons"

	GPIO.output(28,False)
	time.sleep(0.5)
	GPIO.output(28,True)
	time.sleep(0.00001)
	GPIO.output(28,False)
	start = time.time()
	while GPIO.input(30)==0:
		start=time.time()
	while GPIO.input(30)==1:
		stop=time.time()
	elapsed=stop-start
	distance=elapsed*34000
	distance=distance/2
	print "distance %.lf" %distance

	#si la distance avec un objet / mur > 9 cm
	if distance >= 9.0 :
#		connr.send("Moteurs")
		x=data.split(':')
		#envoi de la commande (avance recule etc) + de la valeur de la vitesse
		command.makeMove(x[0],x[1]) #analyse la commande et effectue un mouvement
	else :
	# en cas de detection d'objet
		print "Objet detecte"	
		print distance
		# on arrete le robot
		command.makeMove("0000","0")
#		connr.send("OBJETDETECTE") #echo
		time.sleep(0.3)
		#puis on le fait reculer
		command.makeMove("2222","50")	
conn.close()
