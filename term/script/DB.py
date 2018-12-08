from pico2d import *

import game_framework as gf
import loading_state as lo

class playerInfo:
    def __init__(self):
        self.select = 0
        self.CurHp = 0
        self.Magnize = 0

class stageInfo:
    def __init__(self):
        self.Num = 0
        self.map = 0
        self.structure = 0
        self.enemyCount = 0
        self.bagic_enemy = 0
        self.middle_enemy = 0
        self.boss_enemy = 0

global playerData,stageData
playerData = playerInfo()
stageData = stageInfo()

def enter():
    global playerData, stageData
    print("Data base on!")

    pass

def exit():
	pass

def draw():
    pass

def update():
   pass

def handle_events():
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