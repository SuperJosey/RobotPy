import RPi.GPIO as GPIO

# definition de tous les gpios utilises

def cleangpios():
	GPIO.cleanup()

def setgpios():
	#----------GPIO-Mode-----------
	GPIO.setmode(GPIO.BCM)
	#==============================
	#-------GPIO-Def-Engine--------
	#______Engine_Front_Right______
	GPIO.setup(17, GPIO.OUT) #PWMA
	GPIO.setup(27, GPIO.OUT) #IN1A
	GPIO.setup(22, GPIO.OUT) #IN2A
	#______Engine_Front_Left_______
	GPIO.setup(24, GPIO.OUT) #PWMB
	GPIO.setup(23, GPIO.OUT) #IN1B
	GPIO.setup(18, GPIO.OUT) #IN2B
	#______Engine_Back_Right_______
	GPIO.setup(10, GPIO.OUT)
	GPIO.setup(9, GPIO.OUT)
	GPIO.setup(11, GPIO.OUT)
	#______Engine_Back_Left________
	GPIO.setup(7, GPIO.OUT)
	GPIO.setup(8, GPIO.OUT)
	GPIO.setup(25, GPIO.OUT)
	#________capteurs______________
	GPIO.setup(28, GPIO.OUT)
	GPIO.setup(29, GPIO.OUT)
	GPIO.setup(30, GPIO.IN)
	GPIO.setup(31, GPIO.IN)
	#==============================
	

