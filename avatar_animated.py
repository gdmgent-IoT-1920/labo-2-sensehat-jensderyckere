from sense_hat import SenseHat
from random import randint
import time

sense = SenseHat()

def randomcolor() :
	return (randint(0, 255), randint(0, 255), randint(0, 255))

c = randomcolor()
w = [0, 0, 0]

avatar_one = [
	w, w, w, w, w, w, w, w,
	w, c, c, w, w, c, c, w,	
	w, c, c, w, w, c, c, w,
	w, w, w, w, w, w, w, w,
	w, w, w, w, w, w, w, w,
	w, c, c, c, c, c, c, w,
	w, w, w, w, w, w, w, w,
	w, w, w, w, w, w, w, w,
]

avatar_two = [
	w, w, w, w, w, w, w, w,
	w, c, c, w, w, c, c, w,	
	w, c, c, w, w, w, w, w,
	w, w, w, w, w, w, w, w,
	w, c, w, w, w, w, c, w,
	w, w, c, c, c, c, w, w,
	w, w, w, w, w, w, w, w,
	w, w, w, w, w, w, w, w,
]

avatar_three = [
	w, w, w, w, w, w, w, w,
	w, c, c, w, w, c, c, w,	
	w, c, c, w, w, c, c, w,
	w, w, w, w, w, w, w, w,
	w, w, w, w, w, w, w, w,
	w, w, w, c, c, w, w, w,
	w, w, w, c, c, w, w, w,
	w, w, w, w, w, w, w, w,
]

array = [avatar_one, avatar_two, avatar_three]

while True : 
	for x in array :
		digit = randint(0,2)
		sense.set_pixels(array[digit])
		time.sleep(3)
		sense.clear()