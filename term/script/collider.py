import pico2d
import math

colliderFlag = False

# v1    v2
#     o
# v3    v4

class Collision:
    def __init__(self,object):

        self.target = object

        if self.target.colType =='box':
            #self.left, self.bottom, self.right, self.top = Collision.get_initBox(self)
            #self.v1,self.v2,self.v3,self.v4 = [self.left,self.top],\
             #                                 [self.right,self.top],\
              #                                [self.left,self.bottom],\
               #                               [self.right,self.bottom]
            self.vector = {'v1':[0,0],'v2':[0,0],'v3':[0,0],'v4':[0,0]}
        elif self.target.colType =='circle':
            self.r = self.target.w/2

    def update(self):
        Collision.update_rotBox(self)


    def isCollider(self,other):
        if self.target.colType =='box':
            if other.colType == 'box':
                Collision.update_rotBox(self)
                oL, oB, oR, oT = other.collision.get_rotBox()
                if self.left > oR : return False
                if self.right < oL : return  False
                if self.bottom > oT : return False
                if self.top < oB : return False
                #print(other.name,"is in!!")
                return True
            elif other.colType == 'circle':



                print(other.colType)
                pass
        elif self.target.colType == 'circle':
            if other.colType == 'box':
                pass
            elif other.colType == 'circle':
                UnI = math.sqrt((self.target.x - other.x) ** 2 + (self.target.y - other.y) ** 2)
                if UnI > self.r + other.collision.r: False

                return True
        else:print("this object is None type")

    def get_initBox(self):#여기에다가 다시
        return self.target.x - self.target.w / 2,\
               self.target.y - self.target.h / 2,\
               self.target.x + self.target.w / 2,\
               self.target.y + self.target.h / 2

    def update_rotBox(self):
        self.left, self.bottom, self.right, self.top = Collision.get_initBox(self)

        self.left += math.cos(self.target.rad)
        self.bottom += math.sin(self.target.rad)

        self.right += math.cos(self.target.rad)
        self.top += math.sin(self.target.rad)


    def get_rotBox(self):
        Collision.update_rotBox(self)

        return self.left, self.bottom, self.right, self.top
    def get_rotExtendBox(self,object):
        eL,eB,eR,eT = Collision.get_initBox(self)
        eL,eB,eR,eT = eL - object.collision.r,\
                      eB - object.collision.r,\
                      eR + object.collision.r,\
                      eT + object.collision.r
        eL += math.cos(self.target.rad)
        eB += math.sin(self.target.rad)
        eR += math.cos(self.target.rad)
        eT += math.sin(self.target.rad)
    def update_vetor(self):#delete
        self.v1, self.v2, self.v3, self.v4 = [self.left, self.top], \
                                             [self.right, self.top], \
                                             [self.left, self.bottom], \
                                             [self.right, self.bottom]


def isSearchRange(player, enemy,want):
    #return true, UnI - enemy.searchR return false only false
    UnI = math.sqrt((player.x - enemy.x) ** 2 + (player.y - enemy.y) ** 2)

    if UnI - enemy.searchR <= 0:
        if want == 1:
            return player.x,player.y,enemy.searchR - UnI
        return True
    else:
        return False

def isAttackRange(player, enemy,want):
    UnI = math.sqrt((player.x - enemy.x) ** 2 + (player.y - enemy.y) ** 2)
    if UnI - enemy.attackR <= 0:
        if want == 1:
            return player.x, player.y, enemy.attackR - UnI
        return True
    else:
        return False