#import main module pico2d
from pico2d import *
#define import module
import game_framework as gf
import main_state
#module var initialization
name = "TitleState"
image = None


def enter():
    global image
    open_canvas()
    image = load_image('../resource/title.png')
    
def exit():
    global image
    del(image)
    close_canvas()
def update():
    pass
def draw():
    clear_canvas()
    image.draw(400,300)
    update_canvas()
    
def handle_events():
    events = get_events()
    for e in events:
        if e.type == SDL_QUIT:
            gf.quit()
        else:
            if(e.type,e.key) == (SDL_KEYDOWN,SDLK_ESCAPE):
                gf.quit()
            elif(e.type,e.key) == (SDL_KEYDOWN,SDLK_SPACE):
                gf.change_state(main_state)
def pause():
    pass
def resume():
    pass
