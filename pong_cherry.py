from sense_hat import SenseHat


import pygame
from pygame.locals import *

pygame.init()

sense = SenseHat()
sense.clear()

ball_x=0
ball_y=0

ball_move= sense.set_pixels(ball_x,ball_y)
