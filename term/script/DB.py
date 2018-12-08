from pico2d import *
print("Data base on!")

import game_framework as gf
import loading_state as lo
import stage_control


class playerInfo:
    def __init__(self):
        self.select = 0
        self.CurHp = 0
        self.Magnize = 0

class stageInfo:
    def __init__(self):
        self.stageNum = 0
        self.mapNum = 0
        self.structure = 0
        self.enemyCount = 0
        self.enemySelct = 0
        self.bagic_enemy = 0
        self.middle_enemy = 0
        self.boss_enemy = 0

global playerData,stageData
playerData = playerInfo()
stageData = stageInfo()

def stageSelect(stageNum):
    global stageData
    stageData.stageNum = lo.loadState.stageData[stageNum]["stageNum"]
    stageData.mapNum = lo.loadState.stageData[stageNum]["mapNum"]
    stageData.structure = lo.loadState.stageData[stageNum]["structure"]
    stageData.enemyCount = lo.loadState.stageData[stageNum]["enemyCount"]
    stageData.enemySelct =  lo.loadState.stageData[stageNum]["enemySelect"]
    stageData.bagic_enemy = lo.loadState.stageData[stageNum]["bagic_enemy"]
    stageData.middle_enemy = lo.loadState.stageData[stageNum]["middle_enemy"]
    stageData.boss_enemy = lo.loadState.stageData[stageNum]["boss_enemy"]

def enter():
    global playerData, stageData
    pass

def exit():
    global playerData, stageData
    playerData = None
    stageData = None

    del playerData, stageData
    print("DB exit!!")
    pass


def draw():
    pass

def update():
    stageSelect(0)



    gf.push_state(stage_control)


def handle_events():
    events = get_events()
    for key in events:
        if key.type == SDL_QUIT:
            gf.quit()
        elif (key.type, key.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
            gf.pop_state()


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