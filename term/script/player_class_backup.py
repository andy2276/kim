
#//-----------------/This module's name is 'player_class'/------------------//
#//-----------------/prev module is 'None'/-------------------------------//
#//--------/first,second,third,fourth : import module/--------------------//
#//--------/fifth,sixth : initializing variables/--------------------------//
#//--------/seventh,eighth,ninth : define/---------------------------------//
#//---------------------/Notice End/-----------------------------------------//


#first import pico2d
from pico2d import *
#second import game_framework - keyword 'as' is only use game_framework
import game_framework as gf
#third import next module

#fourth import need module
import math
#fifth initializing module variables(for using to any modul)

#sixth initializing global variables(for only using this module)
running = True
#seventh define class

class clPlayerBody:
    global player,pressing,test,running
    def __init__(self):
        self.pressing = False
        self.keyType = None
        self.x, self.y = 300,200 #X & Y == center's X & Y
        self.hp, self.speed = 10,10.0#state
        self.rotateR, self.rotateL = 0,0#rotate
        self.image = load_image("../res/object/character/player_body_pix.png")
            #loading state 에서 받자        
        self.roImage = None#image

    def draw(self):
        self.image.draw(self.x,self.y)
        self.composite_draw
        
    def update(self):
        if self.pressing == True:
            if self.keyType == SDLK_RIGHT:
                self.x += 2
                
            if self.keyType == SDLK_LEFT:
                self.x -=2
        
    #def handle_event(self):
     #   pass
        


#eighth define function

#ninth redefine game_framework's function
def enter():
    global player
    player = clPlayerBody()
	

def exit():
	pass

def draw():
    global player
    clear_canvas()
    #여기부분 없애기
    player.draw()
    
    update_canvas()
    #여기부분 없애기 어차피 stage에서 모두 클리어후에 작업할것이기 때문에
	

def update():
    global player
    player.update()
    
def handle_events():
    global player
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            gf.quit()
        if event.type ==SDL_KEYDOWN:
            player.pressing = True
            player.keyType = event.key
            
            #왜 끊키는가? 왜 끝까지 가지 못하는가?
        if event.type == SDL_KEYUP:
            player.keyType = None
            player.pressing = False
            

def pause():
	pass

def resume():
	pass
    
#start to this module

if __name__ == '__main__':
	import sys
	glCurrentModule = sys.modules[__name__]	
	open_canvas()
	gf.run(glCurrentModule)
	close_canvas()

