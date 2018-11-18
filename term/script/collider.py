colliderFlag = False

class Collision:
    def __init__(self,object):
        self.target = object

    def update(self):
        print(self.target.x)