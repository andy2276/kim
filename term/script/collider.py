from pico2d import *
import math

colliderFlag = True

# v2    v1
#     o
# v3    v4

def ptInArea(x, y, pts):
    inside = False;
    j = len(pts) - 1
    for i in range(len(pts)):
        xi, yi = pts[i][0], pts[i][1];
        xj, yj = pts[j][0], pts[j][1];

        intersects = ((yi > y) != (yj > y)) and \
                     (x < (xj - xi) * (y - yi) / (yj - yi) + xi)
        if intersects: inside = not inside;
        j = i
    return inside;

class Collision:
    def __init__(self,object):

        self.target = object
        if colliderFlag:
            if self.target.play == 'player':
                self.image = load_image("../res/object/character/player_box.png")
            elif self.target.play == 'enemy':
                self.image = load_image("../res/object/enemy/bagic_enemy_box.png")
            self.im = load_image("../res/object/character/po.png")
        if self.target.colType =='box':
            self.vector = [[0,0],[0,0],[0,0],[0,0]]
        elif self.target.colType =='circle':
            self.r = self.target.w/2

    def draw(self):
        if colliderFlag:
            self.image.composite_draw(self.target.rad,"",self.target.x,self.target.y)
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
                        break
                if self.target.crush == False:
                    self.target.crush = ptInArea(other.x,other.y,self.vector)

                if colliderFlag:
                    if self.target.crush:
                        print("in!!",self.target.name)

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

        extend[0][0] += object.Collision.r
        extend[0][1] += object.Collision.r

        extend[1][0] -= object.Collision.r
        extend[1][1] += object.Collision.r

        extend[2][0] -= object.Collision.r
        extend[2][1] -= object.Collision.r

        extend[3][0] += object.Collision.r
        extend[3][1] -= object.Collision.r

        for v in range(4):
            extend[v][0],extend[v][1]= self.get_matrix(self, extend[v])
        return extend

    def get_matrix(self,vec):
        dx,dy = vec[0]-self.target.x, vec[1]-self.target.y
        #dx, dy = vec[0] , vec[1]
        tx = dx * math.cos(self.target.rad) - dy*math.sin(self.target.rad)
        ty = dx * math.sin(self.target.rad) + dy*math.cos(self.target.rad)
        vec[0]=self.target.x+tx
        vec[1]=self.target.y+ty
        return vec[0],vec[1]


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


