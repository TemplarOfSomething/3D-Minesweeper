from ursina import *
from random import randint
from minefield_logic import logical_minefield_dict_maker as logic

app = Ursina()

mine_dict = logic(5,5,5)

amount = len(mine_dict)
print(mine_dict)

cubes = {}

  

def clicking():
    if mouse.left == True:
        destroy(mouse.hovered_entity)
        print(mouse.world_point)
    elif mouse.right == True:
        mouse.hovered_entity.color = color.red

def flag():
    mouse.hovered_entity.color = color.gray


for z in range(5):
    for y in range(5):
        for x in range(5):
            if mine_dict[(x,y,z)] == '*':
                cubes[(x,y,z)] = Entity(model='cube', collider='box', color=color.red, position=(x,y,z), scale=(1,1,1), on_click=flag)
            elif mine_dict[(x,y,z)] == 1:
                cubes[(x,y,z)] = Entity(model='cube', collider='box', color=color.orange, position=(x,y,z), scale=(1,1,1), on_click=clicking)
            elif mine_dict[(x,y,z)] == 2:
                cubes[(x,y,z)] = Entity(model='cube', collider='box', color=color.yellow, position=(x,y,z), scale=(1,1,1), on_click=clicking)
            elif mine_dict[(x,y,z)] == 3:
                cubes[(x,y,z)] = Entity(model='cube', collider='box', color=color.green, position=(x,y,z), scale=(1,1,1), on_click=clicking)
            elif mine_dict[(x,y,z)] == 4:
                cubes[(x,y,z)] = Entity(model='cube', collider='box', color=color.blue, position=(x,y,z), scale=(1,1,1), on_click=clicking)
            elif mine_dict[(x,y,z)] == 5:
                cubes[(x,y,z)] = Entity(model='cube', collider='box', color=color.magenta, position=(x,y,z), scale=(1,1,1), on_click=clicking)
            elif mine_dict[(x,y,z)] == 6:
                cubes[(x,y,z)] = Entity(model='cube', collider='box', color=color.violet, position=(x,y,z), scale=(1,1,1), on_click=clicking)
            elif mine_dict[(x,y,z)] == 7:
                cubes[(x,y,z)] = Entity(model='cube', collider='box', color=color.azure, position=(x,y,z), scale=(1,1,1), on_click=clicking)
            elif mine_dict[(x,y,z)] == 0:
                cubes[(x,y,z)] = Entity(model='cube', collider='box', color=color.gray, position=(x,y,z), scale=(1,1,1), on_click=clicking)

ec = EditorCamera()
app.run()