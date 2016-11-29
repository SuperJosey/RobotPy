import socket
import RPi.GPIO as GPIO
import time ## Import 'time' library. Allows us to use 'sleep'

#-------------------------GPIO_BOARD_CONFIG---------------------------------
GPIO.setmode(GPIO.BOARD) ## Use board pin numbering
GPIO.setup(7, GPIO.OUT) ## Setup GPIO Pin 7 to OUT
#===========================================================================

#-------------------------TCP_SERVER_CONFIG---------------------------------
HOST = '192.168.1.46'
PORT = 6969
BUFFER_SIZE = 20
#===========================================================================

#------------------------Initialization_Server------------------------------
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1) #Maximum 1 host connected to the socket
#===========================================================================


conn, addr = s.accept()
#print 'Connection address:", addr
while 1:
	data = conn.recv(BUFFER_SIZE)
	if not data: break
	print "received data:", data
	if data == "1111":
		#Marche Avant
		GPIO.output(7,True)
		time.sleep(5)
		GPIO.output(7,False)
	elif data == "2222":
		conn.send(data)
		#Marche Arriere
	elif data == "1221":
		conn.send(data)
		#Rotation dans un sens
	elif data == "2112":
		conn.send(data)
		#Rotation dans un autre sens
	else: 
		conn.send(data)
		print data;
	
	GPIO.cleanup()
	conn.send(data) #echo
conn.close()
