
print("welcome to stage_control!!")
from pico2d import *
import game_framework as gf
import loading_state as lo
import delta_time
import DB as db
import object_control




#selectGlobarVar
Running = True
seletR = None
seletL = None
goUI = None
chooseChar = []
clicked = 0
charNum = 0

stageIn = []

gameFist = True
gameLoof = False

#gameObject_control
gameobject = None
MOVE_TIME = 0.0

BGM = lo.loadSound.bgSound["select_menu"]

def isStageClear():
    global gameobject
    a = 0
    for i in gameobject.enemyList:
        a += 1
    if a == 0:
        return True
    else:
        return False

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
    global seletR, seletL, Running, charNum, clicked, goUI,gameLoof,gameFist,gameobject,MOVE_TIME,bgmTime
    seletR.update()
    seletL.update()
    if goUI.handOn:
        goUI.optionVar = (goUI.optionVar + MOVE_TIME * 10) % 3
    else:
        goUI.optionVar = 0
    goUI.k = ((int)(goUI.optionVar))
    goUI.update()

    if seletR.eventOn:
        clicked += 1
        bgmTime = 0.0
        lo.loadSound.uiSound["select_click"].set_volume(12)
        lo.loadSound.uiSound["select_click"].play(1)
        charNum = clicked % 2
        seletR.clickOff = False
        print(charNum)
    if seletL.eventOn:
        clicked -= 1
        bgmTime = 0.0
        lo.loadSound.uiSound["select_click"].set_volume(12)
        lo.loadSound.uiSound["select_click"].play(1)
        charNum = clicked % 2
        seletL.clickOff = False
        print(charNum)





    if goUI.eventOn:

        print("go!!")
        goUI.clickOff = False

        print(charNum)
        db.playerData.select = charNum
        print(db.playerData.select)
        lo.loadSound.uiSound["menu_click"].set_volume(20)
        lo.loadSound.uiSound["menu_click"].play(1)
        stageEnter()
        gf.change_state(object_control)

    if -2 == clicked or clicked == 2:
        charNum = 0
def stageExit():
    global gameobject


def stageEnter():
    object_control.stageNum = db.stageData.stageNum
    db.stageSelect(db.stageData.stageNum)
    object_control.playerCurHp = db.playerData.CurHp
    object_control.playerCurMagnize = db.playerData.Magnize
    object_control.enemyCount = db.stageData.enemyCount
    object_control.bagicCount = db.stageData.bagic_enemy
    object_control.middleCount = db.stageData.middle_enemy
    object_control.bossCount = db.stageData.boss_enemy


def selectHandle_event(key):
    global seletR, seletL, Running, goUI
    seletR.handle_event(key)
    seletL.handle_event(key)
    goUI.handle_event(key)
def MapDraw(stageNum):
    for m in lo.loadState.mapData[stageNum]:
        x,y,n = m
        lo.loadTerrain[stageNum][n].draw(x,y)
    #print("map create!!")
# def structureDraw(stageNum):
#     for s in  lo.loadState.structData[stageNum]:
#         l,b,x,y = s
#         lo.loadImages.object_structure_image["blocks"].clip_draw(l,b,100,100,x,y)

def enter():
    global gameFist,gameLoof,gameobject

    selectEneter()

def exit():
	pass

def draw():
    global gameFist, gameLoof,gameobject
    clear_canvas()

    selectDraw()
    update_canvas()

global bgmTime
bgmTime = 0.0
def update():
    global gameFist, gameLoof,gameobject,stageIn,BGM,MOVE_TIME,bgmTime
    MOVE_TIME = delta_time.deltaTime()
    selectUdate()
    if bgmTime == 0.0:
        BGM.set_volume(24)
        BGM.play(5)
        bgmTime+=MOVE_TIME
    elif bgmTime >= 16.8:
        bgmTime = 0.0
    else:
        bgmTime += MOVE_TIME

    #print(lo.loadTerrain[0])


def handle_events():
    global Running,gameFist, gameLoof, gameobject

    events = get_events()
    for key in events:
        if key.type == SDL_QUIT:
            gf.quit()
        elif (key.type, key.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
            gf.pop_state()
        else:
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