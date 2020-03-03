from sense_hat import SenseHat
import time
from random import randint

sense = SenseHat()

string = "NMD" 
array = list(string)

def randomcolor() :
	return (randint(0,255), randint(0,255), randint(0,255))

state = False

while state == False :
	for x in array :
		sense.show_letter(x, randomcolor())
		time.sleep(1)

		sense.clear()
	
	time.sleep(3)
