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

def bup():
	global bacx
	global bacxh
	global bacxb
	if (bacx>1):

		bacx-=1
		bacxh=bacx-1
		bacxb=bacx+1
		sense.clear()
		sense.set_pixel(bacxh,7,132,32,87)
		sense.set_pixel(bacx,7,132,32,87)
		sense.set_pixel(bacxb,7,132,32,87)
		sense.set_pixel(ball_x,ball_y,132,32,84)
	
def bdown():
	global bacx
	global bacxh
	global bacxb
	if (bacx<6):

		bacx+=1
		bacxh=bacx-1
		bacxb=bacx+1
		sense.clear()
		sense.set_pixel(bacxh,7,132,32,87)
		sense.set_pixel(bacx,7,132,32,87)
		sense.set_pixel(bacxb,7,132,32,87)
		sense.set_pixel(ball_x,ball_y,132,32,84)


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

	
	if (ballbds==1):
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
		for event in sense.stick.get_events():
			if event.direction=="up":
				bup()
			if event.direction=="down":
				bdown()
	elif (ballhds==1):
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
		for event in sense.stick.get_events():
			if event.direction=="up":
				bup()
			if event.direction=="down":
				bdown()
	elif (ballhgs==1):
		ballhg()
		ball_bouge()
		time.sleep(0.5)
		if (ball_y==7):
			continuer=False
		if (ball_x==0 and ball_y!=7):
			ballhgs=0
			ballbgs=1
		if (ball_y==5 and (ball_x==bacx or ball_x==bacxh or ball_x==bacxb)):
			ballhgs=0
			ballhds=1
		for event in sense.stick.get_events():
			if event.direction=="up":
				bup()
			if event.direction=="down":
				bdown()
	elif (ballbgs==1):
		time.sleep(0.5)
		if (ball_y==7):
			continuer=False
		if (ball_x==6 and ball_y!=7):
			ballbgs=0
			ballhds=1
		if (ball_y==6 and (ball_x==bacx or ball_x==bacxh or ball_x==bacxb)):
			ballbgs=0
			ballbds=1
		for event in sense.stick.get_events():
			if event.direction=="up":
				bup()
			if event.direction=="down":
				bdown()
		
		ballbg() 
		ball_bouge()
	
