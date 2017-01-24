import RPi.GPIO as GPIO
import time
import moteurs

# analyse et effectue une action demande
# receivedCommand est le code de l'action 
# vpwm la valeur pour faire varier le pwm

def makeMove(receivedCommand,vpwm):
# au cas ou plusieurs lignes arrivent d'un coup et la seconde commande soit concatenee avec la valeur de pwm
#	vpwm=int(vpwm)
#	if vpwm > 1000:
#		vpwm=vpwm/10000	

	if receivedCommand == "1111":
		moteurs.goforward()
		time.sleep(0.5)
		moteurs.restAllEngine()
	elif receivedCommand == "2222" :
		moteurs.gobackward()
		time.sleep(0.5)
		moteurs.restAllEngine()
	elif receivedCommand == "1221":
		moteurs.goleft()
		time.sleep(0.5)
		moteurs.restAllEngine()
	elif receivedCommand == "2112":
		moteurs.goright()
		time.sleep(0.5)
		moteurs.restAllEngine()
	else:
		moteurs.restAllEngine()
		return "C_ERR"


def test():
	GPIO.output(7,True)
	time.sleep(5)
	GPIO.output(7,False)
	GPIO.cleanup()

