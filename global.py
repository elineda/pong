from sense_hat import SenseHat
import time

sense=SenseHat()
sense.clear()
ball_x=5
ball_y=3

sense.set_pixel(ball_x,ball_y,132,32,84)

time.sleep(1)

def ball_bouge():
	global ball_x
	global ball_y
	sense.clear()
		
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




while True:
	while (ballbds==1):
		ballbd()
		ball_bouge()
		time.sleep(1)
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
		time.sleep(1)
		
