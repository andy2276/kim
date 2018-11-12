import math

def isSearchRange(player,enemy):
    UnI = math.sqrt((player.x - enemy.x)**2 + (player.y-enemy.y)**2)
    if UnI - enemy.searchR <= 0 :
        
        return True,UnI - enemy.searchR
    else :
        
        return False
        

class te:
    def __init__(self,x,y,sear):
        self.x,self.y = x,y
        self.searchR = sear


#print(math.sqrt(3**2+4**2))

te1 =te(3,4,4)
te2 =te(5,7,2)

that=isSearchRange(te1,te2)
print(that)
