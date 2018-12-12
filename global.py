from sense_hat import SenseHat
import time

sense=SenseHat()
sense.clear()
ball_x=5
ball_y=3

sense.set_pixel(ball_x,ball_y,132,32,84)

bacx=5
bacxh=bacx-1
bacxb=bacx+1

sense.set_pixel(bacxh,7,132,32,87)
sense.set_pixel(bacx,7,132,32,87)
sense.set_pixel(bacxb,7,132,32,87)

def bach():
	if (bacx>0):
		bacx-=1

time.sleep(1)

def ball_bouge():
	global ball_x
	global ball_y
	sense.clear()
	sense.set_pixel(bacxh,7,132,32,87)
	sense.set_pixel(bacx,7,132,32,87)
	sense.set_pixel(bacxb,7,132,32,87)
	sense.set_pixel(ball_x,ball_y,132,32,84)



def ballhg():
	global ball_x
	global ball_y
	ball_x-=1
	ball_y+=1



def ballbg():
	global ball_x
	global ball_y
	ball_x+=1
	ball_y+=1



def ballbd():
	global ball_x
	global ball_y
	ball_x+=1
	ball_y-=1



def ballhd():
	global ball_x
	global ball_y
	ball_x-=1
	ball_y-=1

sense.set_pixel(ball_x,ball_y,132,32,84)

ballbgs=0
ballbds=1
ballhgs=0
ballhds=0


continuer=True



while continuer:

	for event in sense.stick.get_events():
		while (ballbds==1):
			ballbd()
			ball_bouge()
			time.sleep(0.5)
			if (ball_x==7 and ball_y!=0):
				ballbds=0
				ballhds=1
			if (ball_y==0 and ball_x!=7):
				ballbds=0
				ballbgs=1
			if (ball_x==7 and ball_y==0):
				ballbds=0
				ballhgs=1
		while (ballhds==1):
			ballhd()
			ball_bouge()
			time.sleep(0.5)
			if (ball_x==0 and ball_y!=0):
				ballhds=0
				ballbds=1
			if (ball_y==0 and ball_x!=0):
				ballhds=0
				ballhgs=1
			if (ball_x==0 and ball_y==0):
				ballhds=0
				ballbgs=1
		while (ballhgs==1):
			ballhg()
			ball_bouge()
			time.sleep(0.5)
			if (ball_y==7):
				continuer=False
			if (ball_x==0 and ball_y!=7):
				ballhgs=0
				ballbgs=1
		while (ballbgs==1):
			ballbg()
			ball_bouge()
			time.sleep(0.5)
			if (ball_y==7):
				continuer=False
			if (ball_x==7 and ball_y!=7):
				ballbgs=0
				ballhds=1
		if event.direction=="up":
			bacx-=1
			bacxh=bacx-1
			bacxb=bacx+1
			sense.clear()
			sense.set_pixel(bacxh,7,132,32,87)
			sense.set_pixel(bacx,7,132,32,87)
			sense.set_pixel(bacxb,7,132,32,87)
			sense.set_pixel(ball_x,ball_y,132,32,84)
