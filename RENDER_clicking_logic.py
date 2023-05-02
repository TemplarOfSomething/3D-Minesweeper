from ursina import *
import RENDER_minefield_rendering
import MATH_blank_logic
from time import sleep
import math
from MATH_minefield_logic import limited_minefield_dict as logic

cubes = RENDER_minefield_rendering.cubes
mine_dict = RENDER_minefield_rendering.mine_dict
clicked = RENDER_minefield_rendering.clicked


def update():
    if mouse.left == True:
        show_numbers()
        destroy(mouse.hovered_entity)
        sleep(0.25)

    if mouse.right == True:
        mouse.hovered_entity.color = color.orange

def show_numbers():
    global cubes
    for k,v in range(len(MATH_blank_logic.blank_chain_revealer(mine_dict, RENDER_minefield_rendering.round_point()))):
        if v == 0:
            destroy(cubes[k])
        elif v == 1:
            cubes[k].texture = 'img/Tile-1'
        else:
            pass

def round_point():
    x = (clicked[0])
    y = (clicked[1])
    z = (clicked[2])
    point = (x,y,z)
    print(x)
    return point
