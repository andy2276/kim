import math
from pico2d import *
import json

fh = open('object.json','r')

test=json.load(fh)
print(test["player"])