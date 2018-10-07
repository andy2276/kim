#import main module pico2d
from pico2d import *
#define import module
import game_framework as gf
import title_state
import random as rd
#module var initialization
boys = None
grass = None
wp = None
waypoints = None
running = True
count = 0

#define class

class clBoy():
    ani = None
    wp = None
    def __init__(self):
        self.x = rd.randint(0,200)
        self.y = rd.randint(90,550)
        self.speed = 1
        self.frame = rd.randint(0,7)
        self.waypoints = []
        if clBoy.ani == None:
            clBoy.ani = load_image('../resource/run_animation.png')
        if clBoy.wp == None:
            clBoy.wp = load_image('../resource/wp.png')

    def draw(self):
        for wp in self.waypoints:
            self.wp.draw(wp[0], wp[1])
        self.ani.clip_draw(self.frame*100,0,100,100,self.x,self.y)
        
    def update(self):
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
            if(xp,yp) == (self.x,self.y):
                del self.waypoints[0]
        
class clGrass():
    def __init__(self):
        self.image = load_image('../resource/grass.png')
    def draw(self,xa,ya): # class에는 무조건 self를 인자로 주어야한다!
        self.image.draw(xa,ya)

#start game_framework
def handle_events():
    global running
    events = get_events()
    for e in events:
        if e.type == SDL_QUIT:
            gf.quit()
            running = False
        elif e.type == SDL_KEYDOWN:
            if e.key == SDLK_ESCAPE:
                running = False
                gf.change_state(title_state)
        elif e.type == SDL_MOUSEBUTTONDOWN:
            if e.button == 1:
                for b in boys:
                    xp = e.x 
                    yp = 600 - e.y
                    b.waypoints +=[(xp,yp)]
            else:
                for b in boys:
                    b.waypoints = []
num = 1000

def enter():
    global boys,grass,num
    open_canvas()
    boys = [clBoy() for i in range(num)]
    grass = clGrass()
    
def exit():
    global boys, grass
    del(grass)
    del(boys)
def update():
    for b in boys:
         b.update()
def draw():
    clear_canvas()
    grass.draw(400,90)
    for b in boys:
        b.draw()
    update_canvas()
    
if __name__ == '__main__':
	import sys
	glCurrentModule = sys.modules[__name__]	
	open_canvas()
	gf.run(glCurrentModule)
	close_canvas()

    
    
