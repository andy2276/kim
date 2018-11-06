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

action = {"LEFT_RUN": 0, "RIGHT_RUN": 1, "LEFT_STAND": 2, "RIGHT_STAND": 3}
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
    wp = None

    def __init__(self):
        self.name = 'no'
        self.x = 100
        self.y = 90
        self.speed = 1
        self.frame = 0

    def __del__(self):
        pass

        self.state = action["LEFT_STAND"]
        self.go = 1
        if clBoy.ani == None:
            clBoy.ani = load_image('../resource/animation_sheet.png')

    def draw(self):
        self.ani.clip_draw(self.frame * 100, self.state * 100, 100, 100, self.x, self.y)

    def update(self):
        self.frame = (self.frame + 1) % 8




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
            pass
        if e.type == SDL_MOUSEMOTION:
            boy.mx,boy.my = e.x, 600-e.y


num = 5


def enter():
    global boy, grass
    boy = clBoy()
    grass = clGrass()

def exit():
    global boys, grass
    del (grass)
    del (boys)

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



