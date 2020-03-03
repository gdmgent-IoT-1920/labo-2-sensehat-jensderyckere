from sense_hat import SenseHat
import time

sense = SenseHat()

r = [255, 0, 0]
w = [0, 0, 0]

first_rect = [
	w, w, w, w, w, w, w, w,
	w, w, w, w, w, w, w, w,
	w, w, w, w, w, w, w, w,
	w, w, w, w, w, w, w, w,
	w, w, w, w, w, w, w, w,
	w, w, w, w, w, w, w, w,
	w, w, w, w, w, w, w, w,
	w, w, w, w, w, w, w, w,
]

sec_rect = [
	w, w, w, w, w, w, w, w,
	w, w, w, w, w, w, w, w,
	w, w, w, w, w, w, w, w,
	w, w, w, r, r, w, w, w,
	w, w, w, r, r, w, w, w,
	w, w, w, w, w, w, w, w,
	w, w, w, w, w, w, w, w,
	w, w, w, w, w, w, w, w,
]

third_rect = [
	w, w, w, w, w, w, w, w,
	w, w, w, w, w, w, w, w,
	w, w, r, r, r, r, w, w,
	w, w, r, w, w, r, w, w,
	w, w, r, w, w, r, w, w,
	w, w, r, r, r, r, w, w,
	w, w, w, w, w, w, w, w,
	w, w, w, w, w, w, w, w,
]

fou_rect = [
	w, w, w, w, w, w, w, w,
	w, r, r, r, r, r, r, w,
	w, r, w, w, w, w, r, w,
	w, r, w, w, w, w, r, w,
	w, r, w, w, w, w, r, w,
	w, r, w, w, w, w, r, w,
	w, r, r, r, r, r, r, w,
	w, w, w, w, w, w, w, w,
]

fif_rect = [
	r, r, r, r, r, r, r, r,
	r, w, w, w, w, w, w, r,
	r, w, w, w, w, w, w, r,
	r, w, w, w, w, w, w, r,
	r, w, w, w, w, w, w, r,
	r, w, w, w, w, w, w, r,
	r, w, w, w, w, w, w, r,
	r, r, r, r, r, r, r, r,
]

while True : 
	sense.set_pixels(first_rect)
	time.sleep(0.5)
	sense.clear()
	sense.set_pixels(sec_rect)
	time.sleep(0.5)
	sense.clear()
	sense.set_pixels(third_rect)
	time.sleep(0.5)
	sense.clear()
	sense.set_pixels(fou_rect)
	time.sleep(0.5)
	sense.clear()
	sense.set_pixels(fif_rect)
	time.sleep(0.5)
	sense.clear()
	sense.set_pixels(fou_rect)
	time.sleep(0.5)
	sense.clear()
	sense.set_pixels(third_rect)
	time.sleep(0.5)
	sense.clear()
	sense.set_pixels(sec_rect)
	time.sleep(0.5)
	sense.clear()
	sense.set_pixels(first_rect)
	time.sleep(0.5)
	sense.clear()
