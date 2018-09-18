from pico2d import *
import os
import math

os.getcwd()

os.chdir('..')
os.chdir('resource')
os.listdir() #이거 안해주면 읽지를 못함!

open_canvas()

grass = load_image('grass.png')
runCharacer = load_image('run_animation.png')



def squal(speed):
    count = 0
    frame = 0
    x = 0
    y = 90
    while(count != 4):
        clear_canvas()
        grass.draw(400,30) 
        runCharacer.clip_draw(frame * 100,0,100,100,x,y)
        frame = (frame+1)%8
        update_canvas()
        if(count == 0):
            x +=5
            if(x >=770):
                count = 1
        elif(count == 1):
            y+=5
            if(y>=570):
                count=2
        elif(count == 2):
            x -=5
            if(x<=20):
                count = 3
        elif(count == 3):
            y -=5
            if(y<=90):
                return 2
        delay(speed)
        get_events()

def ring(speed):
    ho = 0
    r = 250
    frame = 0
    x = 0
    y = 90
    start_y = start_x = 300
    while(ho != 360):
        clear_canvas()
        grass.draw(400,30)
        runCharacer.clip_draw(frame * 100,0,100,100,x,y)
        ho +=5
        y = math.sin(math.radians(ho))* r + start_y
        x = math.cos(math.radians(ho))* r + start_x
        frame = (frame+1)%8
        update_canvas()
        if(ho == 360):
            return 1
        delay(speed)
        get_events()
        
status = 1
while(True):
    speed = 0.01
    if(status == 1):
        status = squal(speed)
    if(status == 2):
        status = ring(speed)

close_canvas()

