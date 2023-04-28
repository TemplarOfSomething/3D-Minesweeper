from ursina import *
import RENDER_minefield_rendering

app = Ursina()

cubes = RENDER_minefield_rendering.cubes
mine_list = list(RENDER_minefield_rendering.get_list())

global enable_2d
enable_2d = False

global layer
layer = 0


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

def proper_dict(cubes, mine_list):
    for z in range(5):
        for y in range(5):
            for x in range(5):
                if (x,y,z) in mine_list:
                    pass
                else:
                    RENDER_minefield_rendering.cubes[(x,y,z)].enabled = False
    return cubes

def back_to_3d():
    for z in range(5):
        for y in range(5):
            for x in range(5):
                RENDER_minefield_rendering.cubes[(x,y,z)].enabled = True

def input(key):
    global enable_2d
    global layer
    if key == "e":
        if enable_2d:
            back_to_3d()
            enable_2d = False
        else:
            proper_list = proper_list_func(mine_list)
            proper_dict(cubes, proper_list)
            enable_2d = True


    if key == "up arrow":
        if enable_2d: 
            layer += 1
            back_to_3d()
            proper_list = proper_list_func(mine_list)
            proper_dict(cubes, proper_list)

    if key == "down arrow":
        if enable_2d:
            layer -= 1
            back_to_3d()
            proper_list = proper_list_func(mine_list)
            proper_dict(cubes, proper_list)



app.run()