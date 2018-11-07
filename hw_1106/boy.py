# import main module pico2d
from pico2d import *
# define import module
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




class clGrass():
    def __init__(self):
        self.image = load_image('../resource/grass.png')

    def draw(self, xa, ya):  # class에는 무조건 self를 인자로 주어야한다!
        self.image.draw(xa, ya)


# start game_framework
def handle_events():
    global running,boy
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
    global boy, grass
    del (grass)
    del (boy)

def update():
    global boy

    boy.update()


def draw():
    global boy
    clear_canvas()
    grass.draw(400, 90)
    boy.draw();
    update_canvas()


if __name__ == '__main__':
    import sys

    glCurrentModule = sys.modules[__name__]
    open_canvas()
    gf.run(glCurrentModule)
    close_canvas()



