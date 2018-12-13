
print("welcome to menu!!!")
from pico2d import *
import game_framework as gf
import loading_state as lo





# seletR = None
# seletL = None
fontStart = None
#fontReset = None
fontQuit = None

Running = True



def enter():
    global fontStart,fontReset,fontQuit
    # global seletR,seletL
    # seletR = lo.selectUI("selectUI",1100,400,200,200,0)
    # seletL = lo.selectUI("selectUI",100,400,200,200,1)
    fontStart = lo.selectUI("mainFont",760,480,400,95,0)
    #fontReset = lo.selectUI("mainFont", 880, 340, 400, 110, 2)
    fontQuit = lo.selectUI("mainFont", 1000, 200, 400, 107, 1)

    lo.loadSound.bgSound["main_menu"][1].set_volume(48)
    lo.loadSound.bgSound["main_menu"][1].repeat_play()
    #main2 is not used

    delay(1.0)





def exit():
    global fontStart, fontReset, fontQuit
    fontStart = None
    #fontReset = None
    fontQuit = None
    del fontStart, fontQuit
    print("menu exit!!")
    pass


def draw():
    global fontStart, fontReset, fontQuit
    # global seletR,seletL
    clear_canvas()
    lo.loadImages.main_menu_image["background"].draw(lo.CW_HALF,lo.CW_HALF-200)
    fontStart.draw()
    #fontReset.draw()
    fontQuit.draw()
    # seletR.draw()
    # seletL.draw()



    update_canvas()


def update():
    global fontStart, fontReset, fontQuit,Running
    fontStart.update()
    #fontReset.update()
    fontQuit.update()

    if fontStart.eventOn:
        import DB
        gf.change_state(DB)
        lo.loadSound.uiSound["menu_click"].set_volume(5)
        lo.loadSound.uiSound["menu_click"].play(1)
    elif fontQuit.eventOn:
        Running = False
        lo.loadSound.uiSound["menu_click"].set_volume(5)
        lo.loadSound.uiSound["menu_click"].play(1)
        gf.quit()
    pass


def handle_events():
    global fontStart, fontReset, fontQuit,Running
    # global seletR, seletL
    if Running:
        events = get_events()
        for key in events:
            if key.type == SDL_QUIT:
                gf.quit()
            elif (key.type, key.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                gf.pop_state()
            else:
                fontStart.handle_event(key)
                #fontReset.handle_event(key)
                fontQuit.handle_event(key)
        # else:
            # seletR.handle_event(key)
            # seletL.handle_event(key)


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