import math

def isSearchRange(player, enemy):
    #return true, UnI - enemy.searchR return false only false
    UnI = math.sqrt((player.x - enemy.x) ** 2 + (player.y - enemy.y) ** 2)
    if UnI - enemy.searchR <= 0:
        return True, UnI - enemy.searchR
    else:
        return False,0
class collider:
    def __init__(self, xo, yo, coltype, widtho, higho):
        self.x, self.y = xo, yo
        self.w, self.h = widtho, higho
        self.type = coltype
        if self.type == "box":
            collider.box(self, self.w, self.h)
        elif self.type == "circle":
            collider.circle(self, self.w) if self.w == self.h else print("nope!!!")
        else
            self.type = 'controler'
            print("controler")

    def box(self, w, h):
        self.bb = {"LD": [self.x - w / 2, self.y - h / 2], "RU": [self.x + w / 2, self.y + h / 2]}

    def circle(self, r):
        self.bb = {"SP": [self.x, self.y], "HD": [r / 2]}

    def update(self):
        pass

    def isCollider(self,other):
        if other.play == 'player':





a = collider(10, 10, "box", 2, 3)
b = collider(20, 30, "circle", 2, 2)

print(a.bb)