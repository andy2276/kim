from pico2d import *
import game_framework as gf
import json

CW = 1200
CH = 800



mapImage = None
strImage = None

map = []
customMap = []
customStructure = []
rekeys = []
stageNum = 0

toggle  = False
toggleInKey = 0

isStructure = False
mapMaker = None
strMaker = None

# 나의 앵글을 정수로 몫을 뽑는데 90도로 나누면 몇사분면인지 나온다.

class MapMaker():
    def __init__(self):
        self.x,self.y =75,75
        self.w,self.h = 150,150
        self.mapType = 0
    def draw(self):
        map[self.mapType].draw(self.x,self.y)



class StrMapMaker():
    global strImage
    def __init__(self):
        self.x,self.y =50,55
        self.left,self.bottom = 0,0
        self.w,self.h = 100,100
        self.mapType = 0
    def draw(self):
        strImage.clip_draw(self.left,self.bottom,self.w,self.h,self.x,self.y)





def enter():
    global mapImage,mapMaker,isStructure,strImage,strMaker,map
    mapImage = load_image("../res/object/structure/base_fix.png")
    strImage = load_image("../res/object/structure/structure_block_fix.png")
    mapMaker = MapMaker()
    strMaker = StrMapMaker()
    for x in range(3):
        for y in range(3):
            map.append(mapImage.clip_image(mapMaker.w*x,mapMaker.h*y,mapMaker.w,mapMaker.h))

def exit():
	pass

def draw():
    global mapImage, mapMaker,customMap,rekeys,map,strImage,isStructure,strMaker
    clear_canvas()
    for i in rekeys:
        if isStructure:
            l,b,x,y = i
            strImage.clip_draw(l,b,strMaker.w,strMaker.h,x,y)
        else:
            x,y,n = i
            map[n].draw(x,y)


    if isStructure:
        strMaker.draw()
    else:
        mapMaker.draw()

    update_canvas()


def update():
    global toggle,toggleInKey,mapMaker,rekeys,isStructure,strMaker
    if toggle:
        if isStructure:
            psl,psb,psx,psy = strMaker.left,strMaker.bottom,strMaker.x,strMaker.y
        else:
            px, py, pn = mapMaker.x, mapMaker.y, mapMaker.mapType
        if toggleInKey == 1:
            if rekeys == []:
                if isStructure:
                    rekeys.append((psl,psb,psx,psy))
                else:
                    rekeys.append((px, py, pn))
            else:
                troble = False
                for m in rekeys:
                    if isStructure:
                        l,b,x,y =m
                        if psx == x and psy == y:
                            troble = True
                            if psl ==l and psb == b  :
                                print("is Same left and bottom!")
                                break
                        elif psl ==l or psb == b :
                            print("changing this")
                            rekeys.append((psl,psb,psx,psy))
                            rekeys.remove(m)
                            break
                    else:
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
                    if isStructure:
                        rekeys.append((psl, psb, psx, psy))
                    else:
                        rekeys.append((px, py, pn))
        elif toggleInKey == 2:
            for m in rekeys:
                if isStructure:
                    _,_,x,y = m
                    if strMaker.x ==x and strMaker.y == y:
                        rekeys.remove(m)
                        break
                else:
                    x, y, _ = m
                    if mapMaker.x == x and mapMaker.y == y:
                        rekeys.remove(m)
                        break






def handle_events():
    global map,customMap,rekeys,mapMaker,CW,CH,customMap,rekeys,toggle,toggleInKey,stageNum,isStructure,strMaker,\
        customStructure


    events = get_events()
    for key in events:
        if key.type == SDL_QUIT: gf.quit()
        elif (key.type,key.key) == (SDL_KEYDOWN, SDLK_ESCAPE): gf.pop_state()
        elif (key.type) == (SDL_KEYDOWN):
            if key.key == SDLK_1:
                if isStructure:
                    strMaker.left =0
                else:
                    mapMaker.mapType = 0
            elif key.key == SDLK_2:
                if isStructure:
                    strMaker.left = strMaker.w
                else:
                    mapMaker.mapType = 1
            elif key.key == SDLK_3:
                if isStructure:
                    strMaker.left = strMaker.w*2
                else:
                    mapMaker.mapType = 2
            elif key.key == SDLK_4:
                if isStructure:
                    strMaker.left = strMaker.w*3
                else:
                    mapMaker.mapType = 3
            elif key.key == SDLK_5:
                if isStructure:
                    strMaker.left = strMaker.w*4
                else:
                    mapMaker.mapType = 4
            elif key.key == SDLK_6:
                if isStructure:
                    strMaker.left = strMaker.w*5
                else:
                    mapMaker.mapType = 5
            elif key.key == SDLK_7:
                if isStructure:
                    strMaker.left = strMaker.w*6
                else:
                    mapMaker.mapType = 6
            elif key.key == SDLK_8:
                if isStructure:
                    strMaker.left = strMaker.w*7
                else:
                    mapMaker.mapType = 7
            elif key.key == SDLK_9:
                if isStructure:
                    strMaker.left = strMaker.w*8
                else:
                    mapMaker.mapType = 8
            elif key.key == SDLK_0:
                if isStructure:
                    isStructure = False
                    print("structureMaker is",isStructure)
                else:
                    isStructure =True
                    print("structureMaker is", isStructure)
            if isStructure:
                if key.key == SDLK_t:
                    strMaker.bottom +=strMaker.h
                    if strMaker.bottom > 1500:
                        strMaker.bottom -= strMaker.h
                elif key.key == SDLK_g:
                    strMaker.bottom -=strMaker.h
                    if strMaker.bottom < 0:
                        strMaker.bottom += strMaker.h
                elif key.key == SDLK_f:
                    strMaker.left -= strMaker.w
                    if strMaker.left < 0 :
                        strMaker.left +=strMaker.w
                elif key.key == SDLK_h:
                    strMaker.left += strMaker.w
                    if strMaker.left > 1500:
                        strMaker.left -= strMaker.w

            if key.key == SDLK_RIGHT:
                if isStructure:
                    strMaker.x += strMaker.w
                    if strMaker.x >= CW:
                        strMaker.x -= strMaker.w
                else:
                    mapMaker.x += mapMaker.w
                if mapMaker.x >=CW:
                    mapMaker.x -=  mapMaker.w

            elif key.key == SDLK_LEFT:
                if isStructure:
                    strMaker.x -= strMaker.w
                    if strMaker.x <= 0:
                        strMaker.x += strMaker.w
                else:
                    mapMaker.x -=  mapMaker.w
                if mapMaker.x <= 0:
                    mapMaker.x +=  mapMaker.w

            elif key.key == SDLK_UP:
                if isStructure:
                    strMaker.y += strMaker.h
                    if strMaker.y >= CH + strMaker.h:
                        strMaker.y -= strMaker.h
                else:
                    mapMaker.y +=  mapMaker.h
                if mapMaker.y >= CH+mapMaker.h:
                    mapMaker.y -= mapMaker.h

            elif key.key == SDLK_DOWN:
                if isStructure:
                    strMaker.y -= strMaker.h
                    if strMaker.y <= 0:
                        strMaker.y += strMaker.h
                else:
                    mapMaker.y -= mapMaker.h
                if mapMaker.y <= 0:
                    mapMaker.y += mapMaker.h

            if key.key == SDLK_c:
                rekeys = []

            if key.key == SDLK_q:
                if toggle:
                    toggleInKey = 1
                else:toggleInKey= 0

                if isStructure:
                    psl, psb, psx, psy = strMaker.left, strMaker.bottom, strMaker.x, strMaker.y
                else:
                    px,py,pn = mapMaker.x, mapMaker.y, mapMaker.mapType

                if rekeys == []:
                    if isStructure:
                        rekeys.append((psl, psb, psx, psy))
                    else:
                        rekeys.append((px,py,pn))
                else:
                    troble = False
                    for m in rekeys:
                        if isStructure:
                            l,b,x,y = m
                            if psx == x and psy == y:
                                troble = True
                                if psl == l and psb == b:
                                    print("structure you press key q, perfect same!!")
                                    break
                                elif psl != l or psb != b:
                                    print("structure wow different thing,changing")
                                    rekeys.append((psl, psb, psx, psy))
                                    rekeys.remove(m)
                                    break
                        else:
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
                        if isStructure:
                            rekeys.append((psl, psb, psx, psy))
                        else:
                            rekeys.append((px, py, pn))


            elif key.key == SDLK_w:
                for m in rekeys:
                    if isStructure:
                        _,_,x,y = m
                        if strMaker.x == x and strMaker.y == y:
                            rekeys.remove(m)
                            break
                    else:
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
                    if isStructure:
                        customStructure.append(rekeys)
                        print(json.dumps(customStructure,ensure_ascii=False,indent=""))
                        with open("stageInStructure.json",'a',encoding="utf-8")as make_f:
                            json.dump(customStructure,make_f,ensure_ascii=False,indent="")
                            print("structure save done!!")
                    else:
                        customMap.append(rekeys)
                        stageNum +=1
                        print(json.dumps(customMap,ensure_ascii=False,indent="\t"))
                        with open("stageInMap.json",'a',encoding="utf-8")as make_file:
                            json.dump(customMap,make_file,ensure_ascii=False,indent="\t")
                        print("map save done!!")




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