
print("welcome to stage_control!!")
from pico2d import *
import game_framework as gf
import loading_state as lo
import delta_time
import DB as db




#selectGlobarVar
Running = True
seletR = None
seletL = None
goUI = None
chooseChar = []
clicked = 0
charNum = 0

gameFist = True
gameLoof = False

#gameObject_control
gameobject = None


def selectEneter():
    global seletR, seletL, chooseChar, goUI,gameLoof
    seletR = lo.selectUI("selectUI", 1100, 400, 200, 200, 0)
    seletL = lo.selectUI("selectUI", 100, 400, 200, 200, 1)
    goUI = lo.selectUI("goUI", 1000, 100, 200, 120, 0, False)
    chooseChar.append(lo.loadImages.main_menu_image["bagic_player"])
    chooseChar.append(lo.loadImages.main_menu_image["super_player"])


def selectDraw():
    global seletR, seletL, chooseChar, charNum, goUI
    chooseChar[charNum].draw(lo.CW_HALF, lo.CH_HALF)
    seletR.draw()
    seletL.draw()
    goUI.draw()
def selectUdate():
    global seletR, seletL, Running, charNum, clicked, goUI,gameLoof,gameFist,gameobject
    seletR.update()
    seletL.update()
    if goUI.handOn:
        goUI.optionVar = (goUI.optionVar + delta_time.deltaTime() * 10) % 3
    else:
        goUI.optionVar = 0
    goUI.k = ((int)(goUI.optionVar))
    goUI.update()

    if seletR.eventOn:
        clicked += 1

        charNum = clicked % 2
        print(clicked)
        seletR.clickOff = False
    elif seletL.eventOn:
        clicked -= 1
        charNum = clicked % 2
        seletL.clickOff = False

    if goUI.eventOn:
        print("go!!")
        goUI.clickOff = False
        db.playerData.select = charNum
        gameLoof = True
        gameFist = False

        #gf.change_state(object_control)
        import object_control
        gameobject = object_control
        gameobject.playerSelect = charNum
        db.playerData.select = charNum
        gameobject.enemyCount = db.stageData.enemyCount
        print("stage_constrol",db.stageData.enemyCount)
        gameobject.bagicCount = db.stageData.bagic_enemy
        gameobject.middleCount = db.stageData.middle_enemy
        gameobject.bossCount = db.stageData.boss_enemy
        gameobject.enter()


    if -2 == clicked or clicked == 2:
        charNum = 0
def selectHandle_event(key):
    global seletR, seletL, Running, goUI
    seletR.handle_event(key)
    seletL.handle_event(key)
    goUI.handle_event(key)
def MapEnter():
    pass





def enter():
    global gameFist,gameLoof,gameobject
    if gameLoof:
        print("gameEnter!")
    elif gameFist:
        selectEneter()

def exit():
	pass

def draw():
    global gameFist, gameLoof,gameobject
    clear_canvas()
    if gameLoof:
        gameobject.draw()
    elif gameFist:
        selectDraw()

    update_canvas()


def update():
    global gameFist, gameLoof,gameobject
    if gameLoof:
        lo.loadTerrain[db.stageData.mapNum]








        gameobject.update()
    elif gameFist:
        selectUdate()







def handle_events():
    global Running,gameFist, gameLoof, gameobject
    if gameLoof:
        gameobject.handle_events()
    if gameFist:
        events = get_events()
        for key in events:
            if key.type == SDL_QUIT:
                gf.quit()
            elif (key.type, key.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                gf.pop_state()
            else:
                if gameFist:
                    selectHandle_event(key)







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