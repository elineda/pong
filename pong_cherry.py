from sense_hat import SenseHat
import time

sense=SenseHat()
sense.clear()

ball_x=0
ball_y=5

sense.set_pixel(ball_x,ball_y,132,32,84)

x_sens=1
y_sens=-1

def ball_bouge():
  global ball_x
  global ball_y
  time.sleep(0.5)
  sense.clear()
  ball_x=ball_x+x_sens
  ball_y=ball_y+y_sens
  sense.set_pixel(ball_x,ball_y,132,32,84)

bacx=5

sense.set_pixel(bacx,7,132,32,87)

def bac():
  global bacx
  sense.set_pixel(bacx,7,132,32,87)
  sense.set_pixel((bacx+1),7,132,32,87)
  sense.set_pixel((bacx-1),7,132,32,87)
  if (bacx<5):
    sense.set_pixel((bacx+2),7,0,0,0)
  if (bacx>2):
    sense.set_pixel((bacx-2),7,0,0,0)

continuer=True

while continuer:
  ball_bouge()
  bac()
  if (ball_x==7):
    x_sens=-1
  if (ball_x==0):
    x_sens=1
  if (ball_y==0):
    y_sens=1
    
