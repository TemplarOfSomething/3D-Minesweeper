from ursina import *
from MATH_minefield_logic import logical_minefield_dict_maker as logic

app = Ursina()

mine_dict = logic(5,5,5)

amount = len(mine_dict)

global cubes
cubes = {}

  

def clicking():
    if mouse.left == True:
        destroy(mouse.hovered_entity)
        print(mouse.world_point)
    elif mouse.right == True:
        mouse.hovered_entity.color = color.red

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
            elif mine_dict[(x,y,z)] == 1:
                cubes[(x,y,z)] = Entity(model='cube', collider='box', texture='img/Tile-1', position=(x,y,z), scale=(1,1,1), enable=True, on_click=clicking)
            elif mine_dict[(x,y,z)] == 2:
                cubes[(x,y,z)] = Entity(model='cube', collider='box', texture='img/Tile-2', position=(x,y,z), scale=(1,1,1), enable=True, on_click=clicking)
            elif mine_dict[(x,y,z)] == 3:
                cubes[(x,y,z)] = Entity(model='cube', collider='box', texture='img/Tile-3', position=(x,y,z), scale=(1,1,1), enable=True, on_click=clicking)
            elif mine_dict[(x,y,z)] == 4:
                cubes[(x,y,z)] = Entity(model='cube', collider='box', texture='img/Tile-4', position=(x,y,z), scale=(1,1,1), enable=True, on_click=clicking)
            elif mine_dict[(x,y,z)] == 5:
                cubes[(x,y,z)] = Entity(model='cube', collider='box', color=color.magenta, position=(x,y,z), scale=(1,1,1), enable=True, on_click=clicking)
            elif mine_dict[(x,y,z)] == 6:
                cubes[(x,y,z)] = Entity(model='cube', collider='box', color=color.violet, position=(x,y,z), scale=(1,1,1), enable=True, on_click=clicking)
            elif mine_dict[(x,y,z)] == 7:
                cubes[(x,y,z)] = Entity(model='cube', collider='box', color=color.azure, position=(x,y,z), scale=(1,1,1), enable=True, on_click=clicking)
            elif mine_dict[(x,y,z)] == 8:
                cubes[(x,y,z)] = Entity(model='cube', collider='box', color=color.blue, position=(x,y,z), scale=(1,1,1), enable=True, on_click=clicking)
            elif mine_dict[(x,y,z)] == 9:
                cubes[(x,y,z)] = Entity(model='cube', collider='box', color=color.orange, position=(x,y,z), scale=(1,1,1), enable=True, on_click=clicking)
            elif mine_dict[(x,y,z)] == 0:
                cubes[(x,y,z)] = Entity(model='cube', collider='box', texture='img/Tile-Blank', position=(x,y,z), scale=(1,1,1), enable=True, on_click=clicking)



ec = EditorCamera()
Sky(color=color.blue)
#app.run()