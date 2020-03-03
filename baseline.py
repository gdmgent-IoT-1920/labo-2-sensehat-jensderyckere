from sense_hat import SenseHat
from random import randint

sense = SenseHat()

string = "Hello! We Are New Media Development :)"

def randomcolor_back() :
	return (randint(0, 100), randint(0, 100), randint(0, 100))

def randomcolor_front() :
	return (randint(0, 255), randint(0, 255), randint(0, 255))


sense.show_message(string, 0.1, randomcolor_front(), randomcolor_back())

sense.clear()