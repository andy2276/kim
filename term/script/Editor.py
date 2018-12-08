from pico2d import *
import game_framework as gf
import json

CW = 1200
CH = 800



mapImage = None
map = []
customMap = []
rekeys = []
stageNum = 0

toggle  = False
toggleInKey = 0


# 나의 앵글을 정수로 몫을 뽑는데 90도로 나누면 몇사분면인지 나온다.

class MapMaker():
    def __init__(self):
        self.x,self.y =75,75
        self.w,self.h = 150,150
        self.mapType = 0
    def draw(self):
        map[self.mapType].draw(self.x,self.y)





def enter():
    global mapImage,mapMaker
    mapImage = load_image("../res/object/structure/base_fix.png")
    mapMaker = MapMaker()
    for x in range(3):
        for y in range(3):
            map.append(mapImage.clip_image(mapMaker.w*x,mapMaker.h*y,mapMaker.w,mapMaker.h))

def exit():
	pass

def draw():
    global mapImage, mapMaker,customMap,rekeys,map
    clear_canvas()
    for i in rekeys:
        x,y,n = i
        map[n].draw(x,y)

    mapMaker.draw()

    update_canvas()


def update():
    global toggle,toggleInKey,mapMaker,rekeys
    if toggle:
        px, py, pn = mapMaker.x, mapMaker.y, mapMaker.mapType
        if toggleInKey == 1:
            if rekeys == []:
                rekeys.append((px, py, pn))
            else:
                troble = False
                for m in rekeys:
                    x, y, n = m
                    if px == x and py == y:
                        troble = True
                        if pn == n:
                            print("is same!")
                            break
                        elif pn != n:
                            print("is change!")
                            rekeys.append((px, py, pn))
                            rekeys.remove(m)
                            break
                if troble == False:
                    rekeys.append((px, py, pn))
        elif toggleInKey == 2:
            for m in rekeys:
                x, y, _ = m
                if mapMaker.x == x and mapMaker.y == y:
                    rekeys.remove(m)
                    break






def handle_events():
    global map,customMap,rekeys,mapMaker,CW,CH,customMap,rekeys,toggle,toggleInKey,stageNum
    events = get_events()
    for key in events:
        if key.type == SDL_QUIT: gf.quit()
        elif (key.type,key.key) == (SDL_KEYDOWN, SDLK_ESCAPE): gf.pop_state()
        elif (key.type) == (SDL_KEYDOWN):
            if key.key == SDLK_1:
                mapMaker.mapType = 0
            elif key.key == SDLK_2:
                mapMaker.mapType = 1
            elif key.key == SDLK_3:
                mapMaker.mapType = 2
            elif key.key == SDLK_4:
                mapMaker.mapType = 3
            elif key.key == SDLK_5:
                mapMaker.mapType = 4
            elif key.key == SDLK_6:
                mapMaker.mapType = 5
            elif key.key == SDLK_7:
                mapMaker.mapType = 6
            elif key.key == SDLK_8:
                mapMaker.mapType = 7
            elif key.key == SDLK_9:
                mapMaker.mapType = 8


            if key.key == SDLK_RIGHT:
                mapMaker.x += mapMaker.w
                if mapMaker.x >=CW:
                    mapMaker.x -=  mapMaker.w
            elif key.key == SDLK_LEFT:
                mapMaker.x -=  mapMaker.w
                if mapMaker.x <= 0:
                    mapMaker.x +=  mapMaker.w
            elif key.key == SDLK_UP:
                mapMaker.y +=  mapMaker.h
                if mapMaker.y >= CH+mapMaker.h:
                    mapMaker.y -= mapMaker.h
            elif key.key == SDLK_DOWN:
                mapMaker.y -= mapMaker.h
                if mapMaker.y <= 0:
                    mapMaker.y += mapMaker.h

            if key.key == SDLK_q:
                if toggle:
                    toggleInKey = 1
                else:toggleInKey= 0

                px,py,pn = mapMaker.x, mapMaker.y, mapMaker.mapType

                if rekeys == []:
                    rekeys.append((px,py,pn))
                else:
                    troble = False
                    for m in rekeys:
                        x,y,n = m
                        if px == x and py == y :
                            troble = True
                            if pn == n:
                                print("is same!")
                                break
                            elif pn != n:
                                print("is change!")
                                rekeys.append((px, py, pn))
                                rekeys.remove(m)
                                break
                    if troble == False:
                        rekeys.append((px, py, pn))


            elif key.key == SDLK_w:
                for m in rekeys:
                    x,y,_ = m
                    if mapMaker.x == x and mapMaker.y == y:
                        rekeys.remove(m)
                        break
                if toggle:
                    toggleInKey = 2
            elif key.key == SDLK_e:

                if toggle:
                    toggleInKey = 0
                    toggle = False
                elif toggle == False:
                    toggle = True
                print("toggle is ", toggle,"toggle in key is ",toggleInKey)
            elif key.key == SDLK_r:
                if rekeys == []:
                    print("No Date!!! you must injection in rekeys for Data!!")
                else:
                    # with open('stage')
                    customMap.append(rekeys)
                    stageNum +=1
                    print(json.dumps(customMap,ensure_ascii=False,indent="\t"))
                    with open("stageInMap.json",'a',encoding="utf-8")as make_file:
                        json.dump(customMap,make_file,ensure_ascii=False,indent="\t")
                    print("save done!!")




        #print(rekeys)







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