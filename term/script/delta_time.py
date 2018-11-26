from pico2d import *
import time as t


flowTime = 0.0
currTime = 0.0
preTime = 0.0

def deltaTime(isDelay=False,delayTime = -1.0):
    global flowTime, currTime, preTime
    # if preTime == 0.0:
    if isDelay :
        t.sleep(1/60)
    elif delayTime != -1.0:
        t.sleep(delayTime)
    currTime = t.time()
    flowTime = currTime - preTime
    preTime = currTime
    if flowTime==currTime==preTime:
        return 0.03
    return flowTime

def testYourFPS():
    for i in range(60):
        print(deltaTime(True))