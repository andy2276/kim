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

x = 0
y = 0

frame = 0
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
        ho = 0
    delay(speed)
    get_events()


close_canvas()

