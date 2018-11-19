import math
from pico2d import *

open_canvas()
class test:
    def __init__(self):
        self.x,self.y = 100,100
        self.h,self.w = 10,10
        self.rotSpeed = 1/10*math.pi/60
        self.rad = 0
        self.vec = {'a':[0,0],'b':[0,0],'c':[0,0]}



    def draw(self):
        draw_rectangle(*test.get_bb(self))
    def get_bb(self):
        return self.x-5,self.y-5,self.x+5,self.y+5


t = test()
t.vec['a'][0],t.vec['a'][1] = (10,20)










#print(math.sqrt(3**2+4**2))



