from pico2d import *

import game_framework as gf
import json
import object_player
import object_enemy



def enter():
    global player,enemy
    op = open('object.json')
    data = json.load(op)
    d = data['player'][1]
    player = object_player.Player(d["name"],d["x"],d,["hp"],d["rad"],d["rotateSpeed"],d["fowardSpeed"],d["backSpeed"])
    op.close()
    enemy = object_enemy.enemy("bagic_enemy",300,300,90,1,1,0)
def exit():
	pass

def draw():
    global player,enemy
    clear_canvas()
    player.draw()
    enemy.draw()
    update_canvas()

def update():
    global player,enemy
    player.update()
    enemy.update()

def handle_events():
    global player,barrel
    events = get_events()
    for key in events:
        if key.type == SDL_QUIT: gf.quit()
        elif (key.type,key.key) == (SDL_KEYDOWN, SDLK_ESCAPE): gf.pop_state()
        else:
            player.handle_event(key)




def pause():
	pass

def resume():
	pass



if __name__ == '__main__':
    import sys
    glCurrentModule = sys.modules[__name__]
    open_canvas()
    gf.run(glCurrentModule)
    close_canvas()