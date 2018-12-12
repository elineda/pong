from sense_hat import SenseHat
import time
import random
sense=SenseHat()
sense.clear()

ball_x=0
ball_y=5

sense.set_pixel(ball_x,ball_y,132,32,84)

x_sens=1
y_sens=-1
touch=0

def ball_bouge():
  global ball_x
  global ball_y
  global touch
  time.sleep(0.5)
  sense.clear()
  ball_x=ball_x+x_sens
  ball_y=ball_y+y_sens
  sense.set_pixel(ball_x,ball_y,132,32,84)
  if touch==1:
    rdm=random.randint(-1,1)
    ball_x=ball_x+rdm
    touch=0
bacx=4

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
    
def up():
  global bacx
  if bacx>1:
    bacx-=1
    bac()
  
def down():
  global bacx
  if bacx<6:
    bacx+=1
    bac()
continuer=True

while continuer:
  
  if (ball_x==7):
    x_sens=-1
  if (ball_x==0):
    x_sens=1
  if (ball_y==0):
    y_sens=1
  if (ball_y==6 and (ball_x==bacx or ball_x==(bacx+1) or ball_x==(bacx-1))):
    y_sens=-1
    touch=1
  if (ball_y==6) and (ball_x!=bacx and ball_x!=(bacx+1) and ball_x!=(bacx-1)):
    sense.clear()
    sense.show_message("Perdu")
    continuer=False
    break
  for event in sense.stick.get_events():
    if event.direction=="up":
      up()
    if event.direction=="down":
      down()
            
  ball_bouge()
  bac()
