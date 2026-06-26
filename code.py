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