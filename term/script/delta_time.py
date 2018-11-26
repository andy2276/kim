import time

FIRST_TIME = time.gmtime().tm_sec
time.sleep(1/60)

flowTime = 0.0
curTime = 0.0
preTime = time.gmtime().tm_sec

def deltaTime():
    global flowTime,curTime,preTime

    curTime = time.time()
    flowTime = curTime - preTime
    preTime = curTime


# for i in range(100000):
#     deltaTime()
#     print(i,flowTime)

print(preTime-FIRST_TIME)
