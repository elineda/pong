from sense_hat import SenseHat
import time

sense=SenseHat()
sense.clear()


bacx=5
bacxh=bacx-1
bacxb=bacx+1

sense.set_pixel(bacxh,7,132,32,87)
sense.set_pixel(bacx,7,132,32,87)
sense.set_pixel(bacxb,7,132,32,87)



while True:
	for event in sense.stick.get_events():
		if event.direction=="up":
			bacx-=1
			bacxh=bacx-1
			bacxb=bacx+1
			sense.clear()
			sense.set_pixel(bacxh,7,132,32,87)
			sense.set_pixel(bacx,7,132,32,87)
			sense.set_pixel(bacxb,7,132,32,87)
