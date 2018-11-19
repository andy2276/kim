from pico2d import *

import game_framework as gf
import json
import object_player
import object_enemy
import collision
import random
import collider

enemyList = []


def enter():
    global player,enemy
    op = open('object.json')
    data = json.load(op)
    d = data['player'][1]
    player = object_player.Player(d["name"],d["x"],d,["hp"],d["rad"],d["rotateSpeed"],
                                  d["fowardSpeed"],d["backSpeed"],d["width"],d["high"])
    op.close()
    player.collision = collider.Collision(player)
    for i in range(3):
        enemy = object_enemy.enemy("bagic_enemy",random.randint(100,500),300,90,10,10,0,58,78)
        enemy.collision = collider.Collision(enemy)
        enemyList.append(enemy)
        print(enemyList[i].count)
def exit():
	pass

def draw():
    global player,enemy
    clear_canvas()
    player.draw()
    for e in enemyList:
        e.draw()
    update_canvas()

def update():
    global player,enemy
    player.update()
    for e in enemyList:
        e.found = collider.isSearchRange(player,e,0)
        if e.found:
            e.tx,e.ty,e.dist = collider.isSearchRange(player,e,1)
            e.state = 'found'
            e.collision.isCollider(player)
        e.update()


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