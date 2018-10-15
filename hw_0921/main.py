from pico2d import *
import os
import random as rd


open_canvas()

def handle_events():
    global running
    global waypoints
    events = get_events()
    for e in events:
        if e.type == SDL_QUIT:
            running = False
        elif e.type == SDL_KEYDOWN:
            if e.key == SDLK_ESCAPE:
                running = False
        elif e.type == SDL_MOUSEBUTTONDOWN:
            if e.button == 1:
                xp = e.x 
                yp = 600 - e.y
                waypoints += [(xp,yp)]
            else:
                waypoints =[]

class clBoy():
    def __init__(self):
        self.x = rd.randint(0,200)
        self.y = rd.randint(90,550)
        self.speed = rd.randint(1,4)
        self.frame = rd.randint(0,7)
        self.ani = load_image('../resource/run_animation.png')

    def draw(self):
        self.ani.clip_draw(self.frame*100,0,100,100,self.x,self.y)
        
    def update(self,xp,yp):
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
    def nonWaypoints(self):
        self.frame = (self.frame + 1)%8
class clGrass():
    def __init__(self):
        self.image = load_image('../resource/grass.png')
    def draw(self,xa,ya): # class에는 무조건 self를 인자로 주어야한다!
        self.image.draw(xa,ya)

#global initialization
waypoints = []
running = True
#instances initialization
g = clGrass()
wp = load_image('../resource/wp.png')
boys = [clBoy() for i in range(20)]
#while local var initialization
count = 0
while running:
    handle_events()
    if len(waypoints)>0:
        (xp,yp) = waypoints[0]
        for b in boys:
            b.update(xp,yp)
            if(b.x ==xp and b.y == yp):
                count +=1
                if(count == 20):
                    del waypoints[0]
                    count = 0
    else :
        for b in boys:
            b.nonWaypoints()
    clear_canvas()
    for way in waypoints:
        wp.draw(way[0],way[1])
    g.draw(400,90)
    for b in boys:
        b.draw()
    update_canvas()
    
    delay(0.03)

close_canvas()
    
    
    
