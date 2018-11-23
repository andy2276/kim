from pico2d import *
import time as t


flowTime = 0.0
currTime = 0.0
preTime = 0.0

def deltaTime(isDelay):
    global flowTime, currTime, preTime
    # if preTime == 0.0:
    if isDelay :
        t.sleep(1/60)
    currTime = t.time()
    flowTime = currTime - preTime
    preTime = currTime
    if flowTime==currTime==preTime:
        return 0.01
    return flowTime


