from pico2d import *
import os
import random as rd


open_canvas()

def handle_events():
    global running
    global xp,yp
    events = get_events()
    for e in events:
        if e.type == SDL_QUIT:
            running = False
        elif e.type == SDL_KEYDOWN:
            if e.key == SDLK_ESCAPE:
                running = False
        elif e.type == SDL_MOUSEMOTION:
            xp = e.x 
            yp = 600 - e.y

class clBoy():
    def __init__(self):
        self.x = rd.randint(0,200)
        self.y = rd.randint(90,550)
        self.speed = rd.randint(1,4)
        self.frame = rd.randint(0,7)
        self.ani = load_image('../resource/run_animation.png')

    def draw(xp,yp):
        self.ani.clip_draw(self.frame*100,0,100,100,self.x,self.y)
        
    def update(xp,yp):
        self.frame = (self.frame + 1)%8
        if(self.x<=xp and self.y <=yp):
            if(self.x != xp):
                self.x = self.x+self.speed
            if(self.x != yp):
                self.y = self.y +self.speed
        if(self.x<=xp and self.y >=yp):
            if(self.x != xp):
                self.x = self.x+self.speed
            if(self.x != yp):
                self.y = self.y -self.speed
        if(self.x>=xp and self.y <=yp):
            if(self.x != xp):
                self.x = self.x-self.speed
            if(self.x != yp):
                self.y = self.y +self.speed
        if(self.x >= xp and self.y >=yp):
            if(self.x != xp):
                self.x = self.x-self.speed
            if(self.x != yp):
                self.y = self.y -self.speed
class clGrass():
    def __init__(self):
        self.image = load_image('../resource/grass.png')
    
