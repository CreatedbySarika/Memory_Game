import random, pygame ,sys
from pygame.locals import *

# frames persecond
FPS = 30
W_width = 700
W_height = 500
Revealspeed = 8
boxsize = 53
gapsize = 10
B_width = 11
B_height = 6

assert (B_width*B_height)%2==0

xmargin = int (W_width-(B_width*(boxsize+gapsize))/2)
ymargin = int((W_height-(B_height*(boxsize+gapsize))/2))

# colours

GRAY     =   (100,100,100)
NAVYBLUE =   ( 60, 60,100)
WHITE    =   (255,255,255)
RED      =   (255,  0,  0) 
GREEN    =   (  0, 255,   0) 
BLUE     =   (  0,   0, 255) 
YELLOW   =   (255, 255,   0) 
ORANGE   =   (255, 128,   0) 
PURPLE   =   (255,   0, 255) 
CYAN     =   (  0, 255, 255)

bgColor = NAVYBLUE
lbgColor = GRAY
boxColor = WHITE
highlightColor = RED