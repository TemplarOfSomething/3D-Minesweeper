from ursina import *
from MATH_minefield_logic import logical_minefield_dict_maker as logic

Ursina()

mine_dict = logic(5,5,5)

amount = len(mine_dict)

global cubes
cubes = {}

  

def clicking():
    destroy(mouse.hovered_entity)
    print(mouse.world_point)


def flag():
    mouse.hovered_entity.color = color.gray

def get_list():
    global cubes
    return cubes.keys()

for z in range(5):
    for y in range(5):
        for x in range(5):
            if mine_dict[(x,y,z)] == '*':
                cubes[(x,y,z)] = Entity(model='cube', collider='box', color=color.red, position=(x,y,z), scale=(1,1,1), enable=True, on_click=flag)
            else:
                cubes[(x,y,z)] = Entity(model='cube', collider='box', texture='img/Tile-Blank', position=(x,y,z), scale=(1,1,1), enable=True, on_click=clicking)



ec = EditorCamera()
Sky(color=color.blue)
