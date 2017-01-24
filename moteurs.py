import RPi.GPIO as GPIO
import time
from multiprocessing import Process

# Definition des actions des moteurs

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
#==============================

def forwardEngineFL():
	GPIO.output(17, True)
	GPIO.output(27, False)
	GPIO.output(22, True)

def backwardEngineFL():
	GPIO.output(17, True)
	GPIO.output(27, True)
	GPIO.output(22, False)

def forwardEngineFR():
	GPIO.output(24, True)
	GPIO.output(23, False)
	GPIO.output(18, True)

def backwardEngineFR():
	GPIO.output(24, True)
	GPIO.output(23, True)
	GPIO.output(18, False)

def forwardEngineBR():
	GPIO.output(10, True)
	GPIO.output(9, True)
	GPIO.output(11, False)

def backwardEngineBR():
	GPIO.output(10, True)
	GPIO.output(9, False)
	GPIO.output(11, True)

def forwardEngineBL():
	GPIO.output(7, True)
	GPIO.output(8, True)
	GPIO.output(25, False)

def backwardEngineBL():
	GPIO.output(7, True)
	GPIO.output(8, False)
	GPIO.output(25, True)

def restAllEngine():
	GPIO.output(17, False)
	GPIO.output(27, False)
	GPIO.output(22, False)
	GPIO.output(24, False)
	GPIO.output(23, False)
	GPIO.output(18, False)
	GPIO.output(10, False)
	GPIO.output(9, False)
	GPIO.output(11, False)
	GPIO.output(7, False)
	GPIO.output(8, False)
	GPIO.output(25, False)

# Chaque roue dans un process différent
# cela permet d'en lancer plusieurs en parallele a partir des 
# mouvements de base crees plus haut	
	
def goforward():
	m1 = Process(target = forwardEngineFL)
	m2 = Process(target = forwardEngineFR)
	m3 = Process(target = forwardEngineBR)
	m4 = Process(target = forwardEngineBL)
	m1.start()
	m2.start()
	m3.start()
	m4.start()

def gobackward():
	m1 = Process(target = backwardEngineFL)
	m2 = Process(target = backwardEngineFR)
	m3 = Process(target = backwardEngineBR)
	m4 = Process(target = backwardEngineBL)
	m1.start()
	m2.start()
	m3.start()
	m4.start()
 
def goleft():
	m1 = Process(target = forwardEngineFR)
	m2 = Process(target = forwardEngineBR)
	m1.start()
	m2.start()
 
def goright():
	m1 = Process(target = forwardEngineFL)
	m2 = Process(target = forwardEngineBL)
	m1.start()
	m2.start()



#---------Test------------
restAllEngine()
time.sleep(0.5)
restAllEngine()
goright()
time.sleep(0.5)
restAllEngine()

