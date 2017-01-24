import time
import threading
import RPi.GPIO as GPIO

#classe qui aurait du servir pour les capteurs 
#NE FAISAIT PAS PARTIE DE LA PRESENTATION

class Capteur(object):
	
    doStop = False #Does it find an obstacle
    

    def __init__(self, GPIO_TRIGGER, GPIO_ECHO):
        self.GPIO_TRIGGER = GPIO_TRIGGER
        self.GPIO_ECHO = GPIO_ECHO


    def detect(self):
	print "detection?"
        GPIO.output(self.GPIO_TRIGGER, False)

        time.sleep(0.5)

        GPIO.output(self.GPIO_TRIGGER, True)
        time.sleep(0.00001)
        GPIO.output(self.GPIO_TRIGGER, False)
        start = time.time()
        while GPIO.input(self.GPIO_ECHO) == 0:
            start = time.time()
        while GPIO.input(self.GPIO_ECHO) == 1:
            stop = time.time()

        elapsed = stop - start

        distance = elapsed * 34000
        distance = distance / 2

        #print "Distance : %.lf" % distance
        if distance <= 15:
            self.doStop = True
	    print self.GPIO_TRIGGER
	    print "######### %.lf" %distance

    def doDetect(self):
	print "lance le thread"
        threading.Thread(target=self.detect()).start()

    def getDoStop(self):
        return self.doStop
