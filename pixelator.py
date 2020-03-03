from sense_hat import SenseHat
from random import randint
import time

sense = SenseHat()
pixel_list = sense.get_pixels()

x_axis = 0
y_axis = 0

def randomcolor() :
	return [randint(0, 255), randint(0, 255), randint(0, 255)]

while True :
	for x in pixel_list :
		x = randomcolor()

		if x_axis == 7 :
			x_axis = 0
			y_axis += 1

			if y_axis == 8 :
				y_axis = 0

		x_axis += 1
		sense.set_pixel(x_axis, y_axis, x)

		time.sleep(1)
		sense.clear()