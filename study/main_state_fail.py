#import main module pico2d
from pico2d import *
#define import module
import game_framework as gf
import title_state
import random as rd
#module var initialization
boy = None
grass = None
wp = None
waypoints = None
running = True
count = 0

#define class

class clBoy():
    def __init__(self):
        self.x = rd.randint(0,200)
        self.y = rd.randint(90,550)
        self.speed = rd.randint(1,4)
        self.frame = rd.randint(0,7)
        self.waypoints = []
        self.ani = load_image('../resource/run_animation.png')
        self.wp = load_image('../resource/wp.png')

    def draw(self):
        for wp in self.waypoints:
            self.wp.draw(wp[0], wp[1])
        self.ani.clip_draw(self.frame*100,0,100,100,self.x,self.y)
        
    def update(self,xp,yp):
        self.frame = (self.frame + 1)%8
        if len(self.waypoints)>0:
            xp,yp = self.waypoints[0]
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

class clWaypoints():
    def __init__(self):
        self.image = load_image('../resource/wp.png')
    def point(self,xp,yp):
        self.wp += [(xp,yp)]
        return self.wp
    def clearPoint(self):
        self.wp = []
    def delPoint(self):
        del self.wp[0]
    def wpLen(self):
        if(len(self.wp) > 0):
            return len(self.wp)
        else:
            return 0
    def draw():
        for w in self.wp:
            w.draw(w[0],w[1])
        
#start game_framework
def handle_events():
    global running
    global wp
    events = get_events()
    for e in events:
        if e.type == SDL_QUIT:
            running = False
            gf.quit()
        elif e.type == SDL_KEYDOWN:
            if e.key == SDLK_ESCAPE:
                running = False
                gf.change(title_state)
        elif e.type == SDL_MOUSEBUTTONDOWN:
            if e.button == 1:
                xp = e.x 
                yp = 600 - e.y
                wp.point(xp,yp)
            else:
                wp.clearPoint()

def enter():
    global boy,grass,wp
    open_canvas()
    boy = clBoy()
    grass = clGrass()
    wp = clWaypoints()
def exit():
    global boy, grass,wp
    del(boy)
    del(grass)
    del(wp)
def update():
    if (wp.wpLen() > 0):
        (xp,yp) = wp.point()
        for b in boys:
            b.update(xp,yp)
            if(b.x ==xp and b.y == yp):
                count +=1
                if(count == 20):
                    wp.delPoint()
                    count = 0
    else :
        for b in boys:
            b.nonWaypoints()
def draw():
    clear_canvas()
    g.draw(400,90)
    for b in boys:
        b.draw()
    update_canvas()
    
    
    
