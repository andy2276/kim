from pico2d import *

import game_framework as gf
import loading_state as lo
import object_player
import object_enemy
import random
import collider

enemyList = []


def enter():
    global player,enemy
    selectPlayer = 1

    p = lo.loadState.player[selectPlayer]
    player = object_player.Player(p["name"],p['x'],p['y'],p['hp'],p['rad'],p['rotateSpeed'],p['fowardSpeed'],
                                  p['backSpeed'],p['width'],p['high'])

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
        e.found = collider.isInRange(player,e,e.searchR,False)
        #print(e.found)
        if e.found:
            e.attack = collider.isInRange(player, e, e.attackR, False)
            if e.attack:
                e.tx, e.ty, e.dist = collider.isInRange(player, e, e.attackR, True)
                e.state = 'attack'
            else:
                e.tx,e.ty,e.dist = collider.isInRange(player,e,e.searchR,True)
                e.state = 'found'
            #e.collision.isCollider(player)
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
    open_canvas(1200,800)

    gf.run(glCurrentModule)
    close_canvas()