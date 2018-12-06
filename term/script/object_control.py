from pico2d import *

import game_framework as gf
import loading_state as lo
import object_player
import object_enemy
import object_projectile
import object_structure
import random
import collider
import delta_time

TESTINGGAME = False
DELAYTIME = lo.TIMEDELAY

delta_time.set_delay(DELAYTIME)
delta_time.startDeltaTime()
MOVE_TIME = 0



enemyList = []
projectile = []
structure = []

mapNum = []
player = None
enemy = None

test = None

def playerEnter(selectPlayer):
    global player,MOVE_TIME
    p = lo.loadState.player[selectPlayer]
    MOVE_TIME = delta_time.deltaTime()
    object_player.MOVE_TIME = MOVE_TIME
    object_player.TESTINGGAME = TESTINGGAME
    player = object_player.Player(p["name"], p['x'], p['y'], p['hp'], p['rad'], p['rotateSpeed'], p['fowardSpeed'],
                                  p['backSpeed'], p['width'], p['high'])
    player.collision = collider.Collision(player)


def enemyEnter(selectEnemy):
    global enemy,enemyList,MOVE_TIME

    p = lo.loadState.enemy[selectEnemy]
    MOVE_TIME = delta_time.deltaTime()
    object_enemy.MOVE_TIME = MOVE_TIME
    object_enemy.TESTINGGAME = TESTINGGAME
    plus = 10

    for i in range(plus):
        rd = random.randint(1, plus)
        #print(i)
        enemy = object_enemy.enemy(p["name"], p["x"] + (i*40)+200, p["y"] + (i*50)+200, p['rad'], p["rotateForce"], p['SpeedForce'],
                                   p["ai"], p["width"], p['high'])
        plus += 50
        enemy.collision = collider.Collision(enemy)
        enemyList.append(enemy)
def structureEnter():
    global structure
    object_structure.TESTINGGAME = TESTINGGAME
    for i in range(1):
        st = object_structure.Box("test",50+500,500,100,100,"NPC",0,"box",100)
        st.collision = collider.Collision(st)
        structure.append(st)
def mapEnter():
    global mapNum
    for i in range(72):
        mapNum.append((random.randint(0,2),random.randint(0,2)))


def mapDraw():
    global mapNum
    for y in range(12):
        for x in range(6):
            i,j=mapNum[(y*6)+x]
            lo.loadTerrain[i][j].draw((y*150)+75,(x*150)+75)

def enemyUpdate():
    global player, enemy,test,MOVE_TIME

    for e in enemyList:
        #print(e.state,e.blocked)
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
        for ae in enemyList:
            if e.count != ae.count:
                if e.collision.isCollider(ae):
                    e.blocked = collider.isBlocked(ae,e)
                    dist = math.sqrt((ae.x - e.x) ** 2 + (ae.y - e.y) ** 2)
                    tx,ty,dist = collider.isInRange(ae,e,0,True)
                    #print(math.asin(e.visualR/dist))
        EnemyCheckOverlap()
        e.update()



def projectileUpdate():
    global player, enemy, projectile,test,MOVE_TIME
    if player.barrel.attack:
        player.barrel.attack = False
        missiles=object_projectile.cannonball(player.name, player.barrel.gpx, player.barrel.gpy, player.barrel.rad,
                                           "player",300,5,"circle",10,10)
        missiles.collision = collider.Collision(missiles)
        projectile.append(missiles)

    for e in enemyList:
        e.attackCool = MOVE_TIME
        if e.state == 'attack':
            e.attackIdle += e.attackCool
            #enmey attack delay
            if e.attackIdle >=e.attackDelay:
                missiles = object_projectile.missile(e.name, e.x, e.y, e.rad,"enemy",
                                                     100, 20, "box", 10, 10)
                missiles.collision = collider.Collision(missiles)
                projectile.append(missiles)
                e.attackIdle = 0.0


    for m in projectile:
        m.update()
        if m.x <= 0 or m.x >= get_canvas_width() or \
                m.y <= 0 or m.y >= get_canvas_height():
            projectile.remove(m)


    #playerAttackToEnemy
    for m in projectile:
        for e in enemyList:
            if m.collision.isCollider(e):
                if m.play != e.play:
                    enemyList.remove(e)
                    projectile.remove(m)
                    break#리스트 반복을 시키면 안된다.

    #enemyAttackToPlayer
    for m in projectile:
        for e in enemyList:
            if m.collision.isCollider(player):
                if m.play == "enemy":
                    player.hp -= e.damage
                    projectile.remove(m)
                    #print(player.hp)
                    break



def EnemyCheckOverlap():
    global player, enemyList, projectile,structure
    for e in enemyList:
        for a in enemyList:
            if e != a:
                if collider.isInRange(a,e,e.visualR+5,False):
                    dist=math.sqrt((e.x- a.x)**2 + (e.y- a.y)**2)
                    if e.visualR+5 <= dist:
                        a.blocked = True
                        #print(e.blocked)
                        nrad = math.asin(e.visualR/dist)
                        e.tx2 = (math.cos(2*nrad)+e.x)*e.visualR
                        e.ty2 = (math.sin(2*nrad)+e.y)*e.visualR
                    else:
                        nrad = math.atan2(a.y - e.y, a.x - e.x)
                        e.x -= math.cos(nrad) * e.fwForce
                        e.y -= math.sin(nrad) * e.fwForce
                else:
                    e.blocked = False


    structureCheckOverlap()

def structureCheckOverlap():
    global player, enemyList, projectile,structure
    for s in structure:
        for e in enemyList:
            if s.collision.isCollider(e):
                nrad = math.atan2(s.y - e.y, s.x - e.x)
                e.x -= math.cos(nrad)
                e.y -= math.sin(nrad)
                if s.collision.vector[0][0] <= e.tx and e.tx <=s.collision.vector[2][0]:
                    if s.collision.vector[0][1]<=e.ty and e.ty <=s.collision.vector[2][1]:
                        dist = math.sqrt((e.x - s.x) ** 2 + (e.y - s.y) ** 2)
                        math.asin(e.visualR / dist)
                        e.tx2 = (math.cos(2 * nrad) + e.x) * e.visualR
                        e.ty2 = (math.sin(2 * nrad) + e.y) * e.visualR
                e.blocked = True
        if s.collision.isCollider(player):
            player.body.canGo = 0
            if player.body.canGo == 0:
                nrad = math.atan2(s.y - e.y, s.x - e.x)
                player.x -= math.cos(nrad)
                player.y -= math.sin(nrad)
        else: player.body.canGo= 1


def timeUpdate():
    global MOVE_TIME
    print(MOVE_TIME)
    MOVE_TIME = delta_time.deltaTime()

    #print(MOVE_TIME)
    object_player.MOVE_TIME = MOVE_TIME
    #print("player done")
    object_enemy.MOVE_TIME = MOVE_TIME
    #print("enemy done")
    object_projectile.MOVE_TIME = MOVE_TIME
    #print("prohectile done")




    #test-----------
def attackOnject():
    global player, enemy, projectile
    for m in projectile:
        for e in enemyList:
            if m.play == player.play:
                if m.collision.isCollider(e):
                    break

def enter():
    global player,enemy
    mapEnter()
    playerEnter(0)
    enemyEnter(0)
    structureEnter()

def exit():
	pass

def draw():
    global player,enemy,projectile,structure
    clear_canvas()
    mapDraw()
    player.draw()
    for s in structure:
        s.draw()
    for e in enemyList:
        e.draw()
    for m in projectile:
        m.draw()
    update_canvas()


def update():
    global player, enemy, projectile,MOVE_TIME
    #print(delta_time.get_fps())
    timeUpdate()

    player.update()
    projectileUpdate()
    enemyUpdate()
    #print(len(projectile))





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