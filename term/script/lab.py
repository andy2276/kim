import math
from pico2d import *

open_canvas()
class test:
    def __init__(self):
        self.x,self.y = 100,100
        self.h,self.w = 10,10
        self.rotSpeed = 1/10*math.pi/60
        self.rad = 0

    def draw(self):
        draw_rectangle(*test.get_bb(self))
    def get_bb(self):
        return self.x-5,self.y-5,self.x+5,self.y+5




#print(math.sqrt(3**2+4**2))



