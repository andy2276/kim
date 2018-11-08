# import main module pico2d
from pico2d import *
# define import module
import math
import random
import sys

#sys.path.insert(0, '..//hw_0928')
import game_framework as gf
import random as rd

# module var initialization
boy = None
grass = None
wp = None
waypoints = None
running = True
count = 0
FireBall = []

GRAVITY = 10 / 33
BOUNCING_GROUND = 62

# 딕셔너리 멤버 함수 keys(),values(),items()모두 구성 요소를 보여주는 함수

RIGHT_DOWN, LEFT_DOWN, RIGHT_UP, LEFT_UP, TIME_OUT, SPACE_DOWN, ENTER_DOWN = range(7)

key_event_table = {
    (SDL_KEYDOWN, SDLK_RIGHT): RIGHT_DOWN,
    (SDL_KEYDOWN, SDLK_LEFT): LEFT_DOWN,
    (SDL_KEYUP, SDLK_RIGHT): RIGHT_UP,
    (SDL_KEYUP, SDLK_LEFT): LEFT_UP,
    (SDL_KEYDOWN, SDLK_SPACE): SPACE_DOWN,
    (SDL_KEYDOWN, SDLK_RETURN): ENTER_DOWN,
}

# define class
def grave(speed,rad):
    v = speed
    d = rad

    ti = v * math.sin(d*math.pi)/9.8
    hi = (v**2)*(math.sin(d*math.pi))**2/(2*9.8)
    di = (v**2)*(math.sin(d*math.pi))/9.8

    return (ti,hi,di)

class clBall:
    image = None
    def __init__(self,x,y,mx,my):
        self.x,self.y = x,y+20
        self.mx,self.my = mx,my

        self.rad = math.atan2(self.my - self.y, self.mx - self.x)
        self.grav = 0.01
        self.time = 1/60
        self.dist = (math.sqrt((self.mx - self.x) ** 2 + (self.my - self.y) ** 2)) /500000
        #no~~~~~~~~~~~~~~~~~~~~
        self.big = True
        self.sto = False
        self.dx = (self.dist / self.time) * math.cos(self.rad)
        self.dy = (self.dist / self.time) + math.sin(self.rad) - (self.grav * self.time)
        print(self.dx,self.dy)




        if clBall.image == None:
            clBall.image = load_image('../resource/ball21x21.png')
    def draw(self):
        self.image.draw(self.x,self.y)
    def update(self):
        #print(self.dist)
        #self.dx = math.cos(self.rad)
        #self.dy = ((0.0000001 * math.sin(self.rad))-self.grav*1.0*self.time)*self.time
        if self.sto != True:
            self.x += self.dx * self.time
            self.y += self.dy-((self.grav*(self.time**2))/2)
            self.time += 1/30
    def get_bb(self):
        if self.big:
            return self.x - 20, self.y - 20, self.x + 20, self.y + 20
        else:
            return self.x - 10, self.y - 10, self.x + 10, self.y + 10
    def stop(self,a):
        if a == 1:
            self.x,self.y,self.dx,self.dy = 10,20,0,0


class clBoy():
    ani = None
    pointer = None

    def __init__(self):
        self.name = 'no'
        self.x,self.y = 150,150
        self.dx = 0
        self.dy = 0
        self.mx,self.my = 0, 0
        self.dir = 0
        self.speed = 1
        self.frame = 0
        self.state = 3
        self.Fire = []
        if clBoy.ani == None:
            clBoy.ani = load_image('../resource/animation_sheet.png')
            clBoy.pointer = load_image('../resource/pointer.png')
    def __del__(self):
        pass

    def draw(self):
        self.ani.clip_draw(self.frame * 100, self.state * 100, 100, 100, self.x, self.y)
        self.pointer.draw(self.mx,self.my)

    def update(self):
        self.frame = (self.frame + 1) % 8
        if self.x in range(10,800) :
            self.x += self.dx
        else:
            if self.x < 10 :
                self.x += 10
            elif self.x > 700:
                self.x -= 10
    def handle_events(self,e):
        global FireBall
        if(e.type,e.key) in key_event_table:
            key_event = key_event_table[(e.type, e.key)]
            if key_event == RIGHT_DOWN:
                self.state = 1
                self.dx += self.speed
                if self.dx > 0: self.dir = 1
            elif key_event == LEFT_DOWN:
                self.state = 0
                self.dx -= self.speed
                if self.dx < 0: self.dir = 0
            elif key_event == RIGHT_UP:
                self.state = 3
                self.dx -= self.speed
                if self.dx < 0: self.dir = 0
            elif key_event == LEFT_UP:
                self.state = 2
                self.dx += self.speed
                if self.dx > 0: self.dir = 1
            elif key_event == SPACE_DOWN:
                FireBall += [clBall(self.x, self.y, self.mx,self.my)]




class clGrass():
    def __init__(self):
        self.image = load_image('../resource/grass.png')

    def draw(self, xa, ya):  # class에는 무조건 self를 인자로 주어야한다!
        self.image.draw(xa, ya)


# start game_framework
def handle_events():
    global running,boy,FireBall
    events = get_events()
    for e in events:
        if e.type == SDL_QUIT:
            gf.quit()
            running = False
        if (e.type,e.key) in key_event_table:
            boy.handle_events(e)
        if e.type == SDL_MOUSEMOTION:
            boy.mx,boy.my = e.x, 600-e.y


def enter():
    global boy, grass
    boy = clBoy()
    grass = clGrass()

def exit():
    global boy, grass,FireBall
    del (grass)
    del (boy)
    del (FireBall)

def update():
    global boy,FireBall

    boy.update()
    for f in FireBall:
        if (f.x > get_canvas_width() or f.x < 0) and (f.y > get_canvas_height() or f.y <0):
            f.stop(1)
            print("del!!")
        else:
            f.update()

def draw():
    global boy, FireBall
    clear_canvas()
    grass.draw(400, 90)
    boy.draw()
    for f in FireBall:
        f.draw()
    update_canvas()


if __name__ == '__main__':
    import sys

    glCurrentModule = sys.modules[__name__]
    open_canvas()
    gf.run(glCurrentModule)
    close_canvas()



