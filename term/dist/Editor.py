
print("welcome to Edit")
from pico2d import *
import game_framework as gf
import json

#여기는 니가 그릴 캔버스 크기

CW = 1200
CH = 800


#이미지 넣는 부분
mapImage = None
strImage = None
#변수들 여기에서 부르는거라 나중에 건들면됨
map = []
customMap = []
customStructure = []
rekeys = []#실질적으로 이미지가 등록되는 부분
strkeys = []
stageNum = 0

#토글 기능이 있는곳
toggle  = False
toggleInKey = 0

#모드 변환 하는 곳
isStructure = False
mapMaker = None
strMaker = None

# 나의 앵글을 정수로 몫을 뽑는데 90도로 나누면 몇사분면인지 나온다.

#맵 커서
class MapMaker():
    def __init__(self):
        self.x,self.y =75,75
        self.w,self.h = 150,150
        self.mapType = 0
    def draw(self):
        map[self.mapType].draw(self.x,self.y)


#구조물 커서
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
    #이미지 렌더 부분
    mapImage = load_image("../res/object/structure/base_fix.png")
    strImage = load_image("../res/object/structure/structure_block_fix.png")
    mapMaker = MapMaker()
    strMaker = StrMapMaker()
    #맵의 배열 넣는곳
    for x in range(3):
        for y in range(3):
            map.append(mapImage.clip_image(mapMaker.w*x,mapMaker.h*y,mapMaker.w,mapMaker.h))

def exit():
	pass

def draw():
    global mapImage, mapMaker,customMap,rekeys,map,strImage,isStructure,strMaker,strkeys
    clear_canvas()
    if rekeys != []:
        for i in rekeys:
            x, y, n = i
            map[n].draw(x, y)
    if strkeys != []:
        for i in  strkeys:
            l,b,x,y = i
            strImage.clip_draw(l,b,strMaker.w,strMaker.h,x,y)



    if isStructure:
        strMaker.draw()
    else:
        mapMaker.draw()

    update_canvas()


def update():
    global toggle,toggleInKey,mapMaker,rekeys,isStructure,strMaker,strkeys
    if toggle:
        if isStructure:
            psl,psb,psx,psy = strMaker.left,strMaker.bottom,strMaker.x,strMaker.y
        else:
            px, py, pn = mapMaker.x, mapMaker.y, mapMaker.mapType

        if toggleInKey == 1:
            if isStructure:
                if strkeys == []:
                    strkeys.append((psl,psb,psx,psy))
                else:
                    troble = False
                    for m in strkeys:
                        l, b, x, y = m
                        if psx == x and psy == y:
                            troble = True
                            if psl == l and psb == b:
                                print("is Same left and bottom!")
                                break
                            elif psl == l or psb == b:
                                print("changing this")
                                strkeys.append((psl, psb, psx, psy))
                                strkeys.remove(m)
                                break
                    if troble == False:
                        strkeys.append((psl, psb, psx, psy))
            else:
                if rekeys == []:
                    rekeys.append((px, py, pn))
                else:
                    troble = False
                    for m in rekeys:
                        x,y,n = m
                        if px == x and py == y:
                            troble = True
                            if pn == n:
                                print("is same! Number!")
                                break
                            elif pn != n:
                                print("is change!!! map!")
                                rekeys.append((px, py, pn))
                                rekeys.remove(m)
                                break
                    if troble == False:
                        rekeys.append((px, py, pn))
        elif toggleInKey == 2:
                if isStructure:
                    for m in strkeys:
                        _,_,x,y = m
                        if strMaker.x ==x and strMaker.y == y:
                            strkeys.remove(m)
                            break
                else:
                    for m in rekeys:
                        x, y, _ = m
                        if mapMaker.x == x and mapMaker.y == y:
                            rekeys.remove(m)
                            break






def handle_events():
    global map,customMap,rekeys,mapMaker,CW,CH,customMap,rekeys,toggle,toggleInKey,stageNum,isStructure,strMaker,\
        customStructure,strkeys


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
                if isStructure:
                    strkeys = []
                else:
                    rekeys = []

            if key.key == SDLK_q:
                if toggle:
                    toggleInKey = 1
                else:
                    toggleInKey= 0

                if isStructure:
                    psl, psb, psx, psy = strMaker.left, strMaker.bottom, strMaker.x, strMaker.y
                    if strkeys == []:
                        strkeys.append((psl, psb, psx, psy))
                    else:
                        troble = False
                        for m in strkeys:
                            l, b, x, y = m
                            if psx == x and psy == y:
                                troble = True
                                if psl == l and psb == b:
                                    print("structure you press key q, perfect same!!")
                                    break
                                elif psl != l or psb != b:
                                    print("structure wow different thing,changing")
                                    strkeys.append((psl, psb, psx, psy))
                                    strkeys.remove(m)
                                    break
                        if troble == False:
                            strkeys.append((psl, psb, psx, psy))
                else:
                    px, py, pn = mapMaker.x, mapMaker.y, mapMaker.mapType
                    if rekeys == []:
                        rekeys.append((px, py, pn))
                    else:
                        troble = False
                        for m in rekeys:
                            x, y, n = m
                            if px == x and py == y:
                                troble = True
                                if pn == n:
                                    print("is same! Number!")
                                    break
                                elif pn != n:
                                    print("is change!!! map!")
                                    rekeys.append((px, py, pn))
                                    rekeys.remove(m)
                                    break
                        if troble == False:
                            rekeys.append((px, py, pn))
            elif key.key == SDLK_w:
                if isStructure:
                    for m in strkeys:
                        _,_,x,y = m
                        if strMaker.x == x and strMaker.y == y:
                            rekeys.remove(m)
                            break
                else:
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
                if isStructure:
                    if strkeys == []:
                        print("structure None!!!")
                    else:
                        customStructure.append(strkeys)
                        print(json.dumps(customStructure, ensure_ascii=False, indent=""))
                        with open("stageInStructure.json", 'a', encoding="utf-8")as make_f:
                            json.dump(customStructure, make_f)
                            print("structure save done!!")
                else:
                    if rekeys == []:
                        print("map None!!")
                    else:
                        customMap.append(rekeys)
                        stageNum += 1
                        print(json.dumps(customMap, ensure_ascii=False, indent="\t"))
                        with open("stageInMap.json", 'a', encoding="utf-8")as make_file:
                            json.dump(customMap, make_file)
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