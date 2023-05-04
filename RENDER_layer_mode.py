from ursina import *
import RENDER_minefield_rendering
from MATH_minesweeper_mode import *


cubes = RENDER_minefield_rendering.cubes
mine_list = list(RENDER_minefield_rendering.get_list())

global enable_2d
enable_2d = False

global layer
layer = 0

# Returns a list of the keys for the layer user is trying to view

def proper_list_func(mine_list):
    global layer
    if layer > 4:
        layer = 0
    if layer < 0:
        layer = 4
    proper_list = []
    for i in range(125):
        if mine_list[i][1] == layer:
            proper_list.append(mine_list[i])
    return proper_list


# Compares the keys to the dict, and hides all other cubes

def proper_dict(cubes, mine_list):
    for z in range(5):
        for y in range(5):
            for x in range(5):
                if (x,y,z) in mine_list:
                    pass
                else:
                    RENDER_minefield_rendering.cubes[(x,y,z)].enabled = False
    return cubes

# Shows all the cubes again
def back_to_3d():
    for z in range(5):
        for y in range(5):
            for x in range(5):
                RENDER_minefield_rendering.cubes[(x,y,z)].enabled = True

# Waits for input from keyboard

def input(key):
    global enable_2d
    global layer
    # Opens layer mode
    if key == "e":          #or gpiox
        if enable_2d:
            back_to_3d()
            enable_2d = False
        else:
            proper_list = proper_list_func(mine_list)
            proper_dict(cubes, proper_list)
            enable_2d = True
    # Goes up a layer
    if key == "up arrow":
        if enable_2d: 
            layer += 1
            back_to_3d()
            proper_list = proper_list_func(mine_list)
            proper_dict(cubes, proper_list)
    # Goes down a layer
    if key == "down arrow":
        if enable_2d:
            layer -= 1
            back_to_3d()
            proper_list = proper_list_func(mine_list)
            proper_dict(cubes, proper_list)
"""
    if key == "gpioy":        #something like this for sweeping mode
        if mouse.left == True:
            LED = sweeping_mode(mine_dict, clicked_coord)
            requests.put(url=PUT_URL, data={"value":LED})   #for updating LED value
        
"""

