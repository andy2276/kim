#first import pico2d
from pico2d import *
#second import game_framework
import game_framework as gf
#third import next module
import logo_state

#start this module's script
open_canvas()
gf.run(logo_state)
close_canvas()
