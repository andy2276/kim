import pico2d
import math

colliderFlag = False

class Collision:
    def __init__(self,object):

        self.target = object

        if self.target.colType =='box':
            self.left, self.bottom, self.right, self.top = Collision.get_initBox(self)
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
                pass
        else:print("this object is None type")

    def get_initBox(self):
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