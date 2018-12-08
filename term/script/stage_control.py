from pico2d import *
import game_framework as gf
import loading_state as lo
import DB as db


Running = True

seletR = None
seletL = None
chooseChar = []

clicked = 0
charNum = 0

def enter():
    global seletR,seletL,chooseChar
    print("welcome!!!stage_control")
    seletR = lo.selectUI("selectUI",1100,400,200,200,0)
    seletL = lo.selectUI("selectUI",100,400,200,200,1)
    chooseChar.append(lo.loadImages.main_menu_image["bagic_player"])
    chooseChar.append(lo.loadImages.main_menu_image["super_player"])

    pass

def exit():
	pass

def draw():
    global seletR,seletL,chooseChar,charNum
    clear_canvas()
    chooseChar[charNum].draw(lo.CW_HALF,lo.CH_HALF)
    seletR.draw()
    seletL.draw()
    update_canvas()


def update():
    global seletR, seletL, Running,charNum,clicked
    seletR.update()
    seletL.update()
    if seletR.eventOn:
        clicked+=1
        charNum = clicked%2
    elif seletL.eventOn:
        clicked -=1
        charNum = clicked%2

    if -2 == charNum or charNum == 2:
        charNum = 0




def handle_events():
    global seletR, seletL,Running
    if Running:
        events = get_events()
        for key in events:
            if key.type == SDL_QUIT:
                gf.quit()
            elif (key.type, key.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                gf.pop_state()
            else:
                seletR.handle_event(key)
                seletL.handle_event(key)

    pass


def pause():
	pass

def resume():
	pass


if __name__ == '__main__':
    import sys
    glCurrentModule = sys.modules[__name__]
    open_canvas(1200,800)

    gf.run(glCurrentModule)
    close_canvas()