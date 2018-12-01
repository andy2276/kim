import time

FIRST_TIME = time.time()


flowTime = 0.0
curTime = 0.0
preTime = FIRST_TIME
updateCount = 0.0

delayTime = 1/60

def set_delay(option):
    global delayTime
    delayTime = option

def deltaTime():
    global flowTime,curTime,preTime,delayTime,updateCount
    curTime = time.time()
    time.sleep(delayTime)
    frame = curTime - preTime
    preTime = curTime
    flowTime += frame
    updateCount += 0.01
    return frame

def get_fps():
    if flowTime == 0:
        print("err!!!")
        return
    else:
        return ((updateCount*100)/flowTime)



