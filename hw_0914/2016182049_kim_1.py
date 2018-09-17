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

count = 0
x = 0
y = 90
ho = 0
speed = 0.01

r = 250
start_y = start_x = 300

frame = 0
while(count != 4):
    clear_canvas()
    grass.draw(400,30) #grass draw!!
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
            count =0
    
    delay(speed)#speed!!! 1 slow 0.01 faster
    get_events()

close_canvas()
