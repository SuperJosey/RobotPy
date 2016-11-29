import RPi.GPIO as GPIO
import time

def moveForward():
	#Send forward command to motor
	test()

def moveBackward():
	#Send backward command to motor
	test()

def rotateLeft():
	#Send forward command to motors on the right
	#Send backward command to motors on the left
	test()

def rotateRight():
	#Send forward command to mortors on the left
	#Send backward command to motors on the right
	test()

def makeMove(receivedCommand):
	if(receivedCommand == "1111"):
		moveForward() 
	elif(receivedCommand == "2222"):
		moveBackward()
	elif(receivedCommand == "1221"):
		rotateLeft()
	elif(receivedCommand == "2112"):
		rotateRight()
	else:
		return "C_ERR"


def test():
	GPIO.output(7,True)
	time.sleep(5)
	GPIO.output(7,False)
	GPIO.cleanup()

