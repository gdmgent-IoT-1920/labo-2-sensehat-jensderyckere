from sense_hat import SenseHat
import time
sense = SenseHat()


x = 3
y = 0

sense.rotation = 180

sense.set_pixel(x, y, 255, 0, 0)

event = sense.stick.get_events()

while True :
	for event in sense.stick.get_events() :
		if event.direction == 'up' :
			y += 2
			sense.clear()
			sense.set_pixel(x, y, 255, 0, 0)

			time.sleep(0.2)

			y -= 2
			sense.clear()
			sense.set_pixel(x, y, 255, 0, 0)


