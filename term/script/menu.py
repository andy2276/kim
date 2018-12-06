from pico2d import *
import game_framework as gf
import loading_state as lo




seletR = None
seletL = None




def enter():
    global seletR,seletL
    seletR = lo.selectUI("selectUI",1100,400,200,200,0)
    seletL = lo.selectUI("selectUI",100,400,200,200,1)

    pass


def exit():
    pass


def draw():
    global seletR,seletL
    clear_canvas()
    seletR.draw()
    seletL.draw()



    update_canvas()


def update():
    pass


def handle_events():
    global seletR, seletL
    events = get_events()
    for key in events:
        if key.type == SDL_QUIT:
            gf.quit()
        elif (key.type, key.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
            gf.pop_state()
        else:
            seletR.handle_event(key)
            seletL.handle_event(key)


def pause():
    pass


def resume():
    pass


if __name__ == '__main__':
    import sys

    glCurrentModule = sys.modules[__name__]
    open_canvas(1200, 800)

    gf.run(glCurrentModule)
    close_canvas()