from ursina import *
from MATH_minefield_logic import limited_minefield_dict as logic

Ursina()

# Sets up dictionary for mines

mine_dict = logic(5,5,5)

amount = len(mine_dict)

# Where mines go after being created

global cubes
cubes = {}

global clicked
clicked = 0


def flag():
    mouse.hovered_entity.color = color.gray

def get_point():
    global clicked
    clicked = mouse.world_point
    round_point()
    destroy(mouse.hovered_entity)

def round_point():
    x = int(clicked[0])
    y = int(clicked[1])
    z = int(clicked[2])
    point = (x,y,z)
    return point

def get_list():
    global cubes
    return cubes.keys()

for z in range(5):
    for y in range(5):
        for x in range(5):
            if mine_dict[(x,y,z)] == '*':
                cubes[(x,y,z)] = Entity(model='cube', collider='box', texture='img/Tile-Blank', position=(x,y,z), scale=(1,1,1), enable=True, on_click=flag)
            else:
                cubes[(x,y,z)] = Entity(model='cube', collider='box', texture='img/Tile-Blank', position=(x,y,z), scale=(1,1,1), enable=True, on_click=get_point)



ec = EditorCamera()
Sky(texture='background')
