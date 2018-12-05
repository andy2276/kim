from pico2d import *
import math


SEARCH_RANGE = 300
TESTINGGAME = False


# v2    v1
#     o
# v3    v4

def ptInArea(x, y, pts):
    inside = False;
    j = len(pts) - 1
    for i in range(len(pts)):
        xi, yi = pts[i][0], pts[i][1];
        xj, yj = pts[j][0], pts[j][1];

        intersects = ((yi >= y) != (yj >= y)) and \
                     (x <= (xj - xi) * (y - yi) / (yj - yi) + xi)
        if intersects: inside = not inside;
        j = i
    return inside;


def isInRange(tar,me,range,info):
    #여기부분을 다시고치는데, 다른 자료는 건들지 않게 만들자.
    dist = (tar.x - me.x) ** 2 + (tar.y - me.y) ** 2
    if range == 0:
        if (tar.visualR + me.visualR)**2 <= dist:

            if info:
                return tar.x, tar.y, math.sqrt(dist)
            return True
    else:
        if range**2 >= dist:
            if info:
                return tar.x,tar.y,math.sqrt(dist)
            return True
    if info:
        return tar.x, tar.y, math.sqrt(dist)
    return False

def isBlocked(tar,me):
    me.blocked = me.collision.isCollider(tar)




class Collision:
    def __init__(self,object):
        if object == None:
            self.name = 'default'
            self.target,self.colBox = None, None
            self.vector =  [[0,0],[0,0],[0,0],[0,0]]
            self.r = 0
        else:
            self.target = object
            if TESTINGGAME:
                self.collisionFlag = TESTINGGAME
                if self.target.colBox != None:
                    self.colBox = self.target.colBox
                    self.im = load_image("../res/object/character/po.png")
            if self.target.colType =='box':
                self.vector = [[0,0],[0,0],[0,0],[0,0]]
            elif self.target.colType =='circle':
                self.r = self.target.w/2

    def draw(self):
        if TESTINGGAME:
            self.colBox.composite_draw(self.target.rad,"",self.target.x,self.target.y)
            for v in range(4):
                self.im.draw(self.vector[v][0],self.vector[v][1])
        #print(self.target.name,self.vector)
        #print("x y ",self.target.x,self.target.y)

    def update(self):
        Collision.update_rotBox(self)


    def isCollider(self,other):
        if self.target.colType =='box':
            if other.colType == 'box':
                Collision.update_rotBox(self)
                for v in range(4):
                    self.target.crush = ptInArea(other.collision.vector[v][0],
                                                 other.collision.vector[v][1], self.vector)
                    if self.target.crush == True:
                        #print("box crush!!")
                        break

                if self.target.crush == False:
                    self.target.crush = ptInArea(other.x,other.y,self.vector)

                if TESTINGGAME:
                    if self.target.crush:
                        print("in!!",self.target.name)
                return self.target.crush
            elif other.colType == 'circle':
                eV = []
                temp=Collision.get_rotExtendBox(self,other)
                for v in range(4):
                    eV.append(temp[v])

                #if ptInArea(other.x,other.y,eV):
                    #print(self.target.name,"my",self.target.colType,"you",other.colType)

                return self.target.crush
        elif self.target.colType == 'circle':
            if other.colType == 'box':
                eV = []
                temp = Collision.get_rotExtendOtherBox(self,other)
                for v in range(4):
                    eV.append(temp[v])
                self.target.crush = ptInArea(self.target.x,self.target.y,eV)
                #if self.target.crush :
                    #print(self.target.crush, self.target.name, "my", self.target.colType, "you", other.colType)
                return ptInArea(self.target.x,self.target.y,eV)
            elif other.colType == 'circle':
                dist = (self.target.x - other.x) ** 2 + (self.target.y - other.y) ** 2
                if (self.target.r + other.r)**2 <= dist:
                    self.target.crush = False
                    return False
                self.target.crush = True
                return True

        else:print("this object is None type")

    def get_initBox(self):
        return [self.target.x + self.target.w / 2, self.target.y + self.target.h / 2],\
               [self.target.x - self.target.w / 2, self.target.y + self.target.h / 2],\
               [self.target.x - self.target.w / 2, self.target.y - self.target.h / 2],\
               [self.target.x + self.target.w / 2, self.target.y - self.target.h / 2]


    def update_rotBox(self):
        newVector = Collision.get_initBox(self)
        for v in range(4):
            self.vector[v] = newVector[v]
            self.vector[v][0],self.vector[v][1]=Collision.get_matrix(self,self.vector[v])

    def get_rotBox(self):
        Collision.update_rotBox(self)

        return

    def get_rotExtendBox(self,object):
        extend = Collision.get_initBox(self)

        extend[0][0] += object.r
        extend[0][1] += object.r

        extend[1][0] -= object.r
        extend[1][1] += object.r

        extend[2][0] -= object.r
        extend[2][1] -= object.r

        extend[3][0] += object.r
        extend[3][1] -= object.r

        for v in range(4):
            extend[v][0],extend[v][1]= self.get_matrix( extend[v])
        return extend

    def get_rotExtendOtherBox(self, object):
        extend = Collision.get_initBox(object.collision)

        extend[0][0] += self.r
        extend[0][1] += self.r

        extend[1][0] -= self.r
        extend[1][1] += self.r

        extend[2][0] -= self.r
        extend[2][1] -= self.r

        extend[3][0] += self.r
        extend[3][1] -= self.r

        for v in range(4):
            extend[v][0], extend[v][1] = object.collision.get_matrix(extend[v])

        return extend

    def get_matrix(self,vec):
        dx,dy = vec[0]-self.target.x, vec[1]-self.target.y
        #dx, dy = vec[0] , vec[1]
        tx = dx * math.cos(self.target.rad) - dy*math.sin(self.target.rad)
        ty = dx * math.sin(self.target.rad) + dy*math.cos(self.target.rad)
        vec[0]=self.target.x+tx
        vec[1]=self.target.y+ty
        return vec[0],vec[1]

    def set_tempCollision(self,obj):
        self.target = obj

def haveCollision(obj):
        return True if obj.collision != None else False





#def isSearchRange(player, enemy,want):
 #   #return true, UnI - enemy.searchR return false only false
  #  UnI = math.sqrt((player.x - enemy.x) ** 2 + (player.y - enemy.y) ** 2)
#
 #   if UnI - enemy.searchR <= 0:
  #      if want == 1:
   #         return player.x,player.y,enemy.searchR - UnI
    #    return True
#    else:
 #       return False
#def isSearchRange(target, enemy,info,range):
 #   #return true, UnI - enemy.searchR return false only false
  #  UnI =(target.x - enemy.x) ** 2 + (target.y - enemy.y) ** 2
   # if  (target.visualR**2)+ (range**2) <= UnI:
    #    if info:
     #       return target.x,target.y,range-math.sqrt(UnI)
      #  return True
#    else:
 #       return False



#무조건 플레이어의 입장에서 계산을 하자.

