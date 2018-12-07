from pico2d import *
import game_framework as gf
import math
import loading_state as lo

CW = 1200
CH = 800



mapImage = None
map = []
customMap = []
rekeys = []

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
   pass

def handle_events():
    global map,customMap,rekeys,mapMaker,CW,CH,customMap,rekeys,toggle,toggleInKey
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

                createMap = (mapMaker.x, mapMaker.y, mapMaker.mapType)
                if rekeys == []:
                    rekeys.append(createMap)
                else:
                    for m in rekeys:
                        x,y,n = m
                        if (mapMaker.x == x and mapMaker.y == y):
                            if mapMaker.mapType != n:
                                rekeys.remove(m)
                                rekeys.append(createMap)
                                break
                        elif (mapMaker.x != x and mapMaker.y != y):
                            rekeys.append(createMap)

            elif key.key == SDLK_w:
                for m in rekeys:
                    x,y,n = m
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
            elif key.key == SDLK_r:
                pass
    count = 0
    for i in rekeys:
        count +=1
        print(count)







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