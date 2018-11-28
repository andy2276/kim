from pico2d import *

import game_framework as gf
import loading_state as lo
import object_player
import object_enemy
import object_projectile
import random
import collider

enemyList = []
projectile = []
player = None
enemy = None


def playerEnter(selectPlayer):
    global player
    p = lo.loadState.player[selectPlayer]
    player = object_player.Player(p["name"], p['x'], p['y'], p['hp'], p['rad'], p['rotateSpeed'], p['fowardSpeed'],
                                  p['backSpeed'], p['width'], p['high'])
    player.collision = collider.Collision(player)

def enemyEnter(selectEnemy):
    global enemy,enemyList
    p = lo.loadState.enemy[selectEnemy]
    for i in range(10):
        rd = random.randint(200, 500)
        enemy = object_enemy.enemy(p["name"], p["x"] + rd, p["y"] + rd, p['rad'], p["rotateForce"], p['SpeedForce'],
                                   p["ai"], p["width"], p['high'])
        enemy.collision = collider.Collision(enemy)
        enemyList.append(enemy)

def enemyUpdate():
    global player, enemy
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

def projectileUpdate():
    global player, enemy






def enter():
    global player,enemy
    playerEnter(1)
    enemyEnter(0)

def exit():
	pass

def draw():
    global player,enemy,projectile
    clear_canvas()
    player.draw()
    for e in enemyList:
        e.draw()
    for m in projectile:
        m.draw()
    update_canvas()


def update():
    global player, enemy, projectile
    player.update()
    if player.barrel.attack:
        player.barrel.attack = False
        missiles=object_projectile.missile(player.name,player.barrel.gpx,player.barrel.gpy,player.barrel.rad,
                                           "player",100,20,"circle",10,10)
        print("ok!")
        missiles.collision = collider.Collision(missiles)
        projectile.append(missiles)
    enemyUpdate()
    print(len(projectile))
    for m in projectile:
        m.update()
        if m.x <= 0 or m.x >= get_canvas_width() or\
                m.y <= 0 or m.y >= get_canvas_height():
            projectile.remove(m)




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