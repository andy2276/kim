from pico2d import *

print("welcom to object_constrol")
import game_framework as gf
import loading_state as lo
import object_player
import object_enemy
import object_projectile
import object_structure
import random
import collider
import delta_time
import stage_control
import DB as db



# global TESTINGGAME,DELAYTIME,MOVE_TIME
#testVar
TESTINGGAME = False
#timeVar
DELAYTIME = 1/120

delta_time.set_delay(DELAYTIME)
delta_time.startDeltaTime()
global MOVE_TIME
MOVE_TIME = 0
#createVar
enemyList = []
projectile = []
structure = []
mapNum = []
player = None
enemy = None
test = None
clearCount = 0
pp = load_image('../res/object/character/po.png')

#interface var to DB
#player
playerSelect = 0
playerCurHp = 0
playerCurMagnize = 0

#stage
stageNum = 0
enemyCount =0
bagicCount = 0
middleCount =0
bossCount = 0
# def stageEnter():
#     global playerSelect,playerCurHp,playerCurMagnize,stageNum,enemyCount,bagicCount,middleCount,bossCount


def playerEnter(selectPlayer):
    global player,MOVE_TIME
    p = lo.loadState.player[selectPlayer]
    MOVE_TIME = delta_time.deltaTime()
    object_player.MOVE_TIME = MOVE_TIME
    object_player.TESTINGGAME = TESTINGGAME
    player = object_player.Player(p["name"], p['x'], p['y'], p['hp'], p['rad'], p['rotateSpeed'], p['fowardSpeed'],
                                  p['backSpeed'], p['width'], p['high'])
    player.collision = collider.Collision(player)


def enemyEnter(selectEnemy,countEnenmy):
    global enemy,enemyList,MOVE_TIME
    p = lo.loadState.enemy[selectEnemy]
    MOVE_TIME = delta_time.deltaTime()
    object_enemy.MOVE_TIME = MOVE_TIME
    object_enemy.TESTINGGAME = TESTINGGAME
    for i in range(countEnenmy):

        enemy = object_enemy.enemy(p["name"], p["x"] +450 +(random.randint(100,200)*random.randint(-1,1)), p["y"] +450 +(random.randint(100,200)*random.randint(-1,1)), p['rad'], p["rotateForce"], p['SpeedForce'],
                                   p["ai"], p["width"], p['high'],p["attackDelay"])
        enemy.collision = collider.Collision(enemy)
        enemyList.append(enemy)
def structureEnter(stageN):
    global structure
    object_structure.TESTINGGAME = TESTINGGAME
    for i in lo.loadState.structData[stageN]:
        l,d,x,y = i
        st = object_structure.Box("box",l,d,x,y,100,100,"NPC","box",100)
        st.collision = collider.Collision(st)
        structure.append(st)
# def mapEnter():
#     global mapNum
#     for i in range(72):
#         mapNum.append((random.randint(0,2),random.randint(0,2)))
def playerUpdate():
    global player, enemy, test, MOVE_TIME,projectile
    player.update()
    if player.barrel.attack:
        player.barrel.attack = False
        missiles=object_projectile.projectile(player.name,"missile", player.barrel.gpx, player.barrel.gpy, player.barrel.rad,
                                           "player",500,10,100,"circle",10,10)
        missiles.collision = collider.Collision(missiles)
        projectile.append(missiles)

    if lo.C_WIDTH < player.x or player.x < 0:
        player.body.x += -math.cos(player.rad)*20
        print("x out!")
    if lo.C_HIEGHT < player.y or player.y < 0:
        player.body.y += -math.sin(player.rad)*20
        print("y out!")



def enemyUpdate():
    global player, enemy,test,MOVE_TIME,pp

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

            e.attackCool = MOVE_TIME
            if e.state == 'attack':
                e.attackIdle += e.attackCool
                # enmey attack delay
                if e.attackIdle >= e.attackDelay:
                    missiles = object_projectile.projectile(e.name,"cannonball", e.x, e.y, e.rad, "enemy",
                                                         500, 20, 10,"box", 10, 10)
                    missiles.collision = collider.Collision(missiles)
                    projectile.append(missiles)
                    e.attackIdle = 0.0






        # if lo.C_WIDTH-100 < e.x < 100 :
        #     e.x += -math.cos(e.rad)
        #     print("what?x")
        # if lo.C_HIEGHT-100 < e.y < 100:
        #     e.y += -math.sin(e.rad)
        #     print("what?y")

        # if lo.C_WIDTH < e.tx < 0

        for s in structure:
            if s.collision.vector[2][0] <= e.tx<= s.collision.vector[0][0] and\
                    s.collision.vector[2][1] <= e.ty<= s.collision.vector[0][1]:
                e.tx = s.x + random.randint(-1, 1) * s.w
                e.ty = s.y + random.randint(-1, 1)* s.h
                print(e.tx,e.ty)

        if lo.C_WIDTH < e.x or e.x < 0:
            e.x += -math.cos(e.rad)
        if lo.C_HIEGHT-50 < e.y or e.y < 0:
            e.y += -math.sin(e.rad)


        # if (-e.ai <= e.x - e.tx <= e.ai) or (-e.ai <= e.y - e.ty <= e.ai):
        #     e.collisionTime += MOVE_TIME
        #     if e.collisionTime > 3.0:
        #         print(e.count, "doesnt", e.x - e.tx, e.y - e.ty)
        #         e.tx += random.randint(-50, 50)
        #         e.ty += random.randint(-50, 50)
        # else:
        #     e.collisionTime = 0.0




        EnemyCheckOverlap()
        e.update()



def projectileUpdate():
    global player, enemy, projectile,test,MOVE_TIME,structure,projectile

    for s in structure:
        for m in projectile:
            if m.collision.isCollider(s):
                projectile.remove(m)
                if m.play == "player":
                    s.x -= math.cos(m.rad) * m.damage*0.1
                    s.y -= math.sin(m.rad) * m.damage*0.1
                elif m.play == "enemy":
                    s.x += math.cos(m.rad) * m.damage * 0.1
                    s.y += math.sin(m.rad) * m.damage * 0.1
                break
    for m in projectile:
        m.update()
        if m.x <= 0 or m.x >= get_canvas_width() or \
                m.y <= 0 or m.y >= get_canvas_height():
            projectile.remove(m)
            print("out!!")
            break
    #playerAttackToEnemy
    for m in projectile:
        for e in enemyList:
            if m.collision.isCollider(e):
                if m.play != e.play:
                    e.hp -= m.damage
                    e.x -= math.cos(m.rad) * e.fwForce*m.damage
                    e.y -= math.sin(m.rad) * e.fwForce*m.damage
                    if e.hp <= 0:
                        enemyList.remove(e)
                    projectile.remove(m)
                    break#리스트 반복을 시키면 안된다.
        for e in enemyList:
            if m.collision.isCollider(player):
                if m.play == "enemy":
                    player.hp -= m.damage
                    print(player.hp)
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
                nrad = math.atan2(s.y - player.y, s.x - player.x)
                player.body.x -= math.cos(nrad)
                player.body.y -= math.sin(nrad)
        else: player.body.canGo= 1

def myInfo():
    global playerSelect, playerCurHp, playerCurMagnize,stageNum,player
    playerCurHp = player.hp
    return stageNum,playerSelect,playerCurHp,playerCurMagnize

def MapDraw(stageNum):
    for m in lo.loadState.mapData[stageNum]:
        x,y,n = m
        lo.loadTerrain[stageNum][n].draw(x,y)

def timeUpdate():
    global MOVE_TIME
    #print(MOVE_TIME)
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


def isStageClear():
    global enemyList
    a = 0
    for i in enemyList:
        a += 1
    if a == 0:
        return True
    else:
        return False


def nextStage(stageN):
    global playerSelect,playerCurHp,playerCurMagnize,stageNum,enemyCount,bagicCount,middleCount,bossCount,clearCount,\
        enemyList,projectile,structure,mapNum,player,enemy
    db.stageData.stageNum,db.playerData.select,db.playerData.CurHp,db.playerData.Magnize = myInfo()
    clearCount += delta_time.deltaTime()
    if clearCount >= 1.0:
        stageNum = stageN
        db.stageSelect(stageNum)
        playerSelect = db.playerData.select
        playerCurHp = db.playerData.CurHp
        playerCurMagnize = db.playerData.Magnize
            # stage
        stageNum = db.stageData.stageNum
        enemyCount = db.stageData.enemyCount
        bagicCount = db.stageData.bagic_enemy
        middleCount = db.stageData.middle_enemy
        bossCount = db.stageData.boss_enemy
        print(stageNum,playerSelect,playerCurHp,playerCurMagnize,stageNum,enemyCount)
        enemyList = []
        projectile = []
        structure = []
        mapNum = []
        player = None
        enemy = None
        enter()
def enter():
    global player,enemy,test,playerSelect,bagicCount,middleCount,bossCount,stageNum
    db.stageSelect(stageNum)
    #mapEnter()
    playerEnter(db.playerData.select)
    if bagicCount != 0:
        enemyEnter(0,bagicCount)
    if middleCount != 0:
        enemyEnter(1, bagicCount)
    if bossCount !=0 :
        enemyEnter(2,bossCount)
    structureEnter(stageNum)
    test = lo.UI("battleUI", 1100, 50, 200, 100, 0)


def exit():
    global playerSelect,playerCurHp,playerCurMagnize, player, enemy, test, MOVE_TIME,projectile,stageNum
    print("objectControl exit!!")
    MOVE_TIME = 0
    # createVar
    enemyList = []
    projectile = []
    structure = []
    mapNum = []
    player = None
    enemy = None
    test = None

    del playerSelect,playerCurHp,playerCurMagnize, player, enemy, test, MOVE_TIME,projectile,stageNum
    import sys
    sys.exit()





def draw():
    global player,enemy,projectile,structure,test,pp
    clear_canvas()
    if isStageClear():
        lo.loadImages.main_menu_image["stageClear"].draw(lo.CW_HALF, lo.CH_HALF)
    else:
        MapDraw(stageNum)
        print("what the?!",stageNum)
        player.draw()
    # test.draw()
        for s in structure:
            s.draw()
        for e in enemyList:
            e.draw()
            #pp.draw(e.tx, e.ty)
        for m in projectile:
            m.draw()


    update_canvas()


def update():
    global player, enemy, projectile,MOVE_TIME,test,enemyList,clearCount,stageNum
    #print(delta_time.get_fps())
    timeUpdate()
    #print(test.handOn,test.clickOn,test.eventOn)

    # if test.eventOn:
    #     print("event On!!!")

    projectileUpdate()
    playerUpdate()
    enemyUpdate()
    if isStageClear():
        volotaile = stageNum+1
        nextStage(volotaile)

    #print(len(projectile))



def handle_events():
    global player,barrel,test
    events = get_events()
    for key in events:
        if key.type == SDL_QUIT: gf.quit()
        elif (key.type,key.key) == (SDL_KEYDOWN, SDLK_ESCAPE): gf.pop_state()
        else:
            player.handle_event(key)
            test.handle_event(key)

def pause():
	pass

def resume():
	pass


if __name__ == '__main__':
    import sys
    glCurrentModule = sys.modules[__name__]
    open_canvas(1200,800)
    import game_framework as gf
    gf.run(glCurrentModule)
    close_canvas()