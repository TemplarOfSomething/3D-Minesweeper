from ursina import *
from MATH_minefield_logic import limited_minefield_dict as logic

app = Ursina()

# Sets up dictionary for mines

mine_dict = logic(5,5,5)

amount = len(mine_dict)

# Where mines go after being created

global cubes
cubes = {}

# Coordinate variable

global clicked
clicked = 0

# Counts the number of flags the user has at their disposal

global flag_count
flag_count = 1

# Shows number of flags left

flags = Text(text=flag_count, scale=2, origin=(14,-8))

# Gets the mouse coordinate

def get_point():
    global clicked
    clicked = mouse.world_point
    round_point()

# Makes coordinate into a readable number

def round_point():
    global point
    x = int(clicked[0])
    y = int(clicked[1])
    z = int(clicked[2])
    point = (x,y,z)

# Returns a list of all the keys in the cubes dictionary

def get_list():
    global cubes
    return cubes.keys()

# makes cubes

for z in range(5):
    for y in range(5):
        for x in range(5):
            if mine_dict[(x,y,z)] == '*':
                cubes[(x,y,z)] = Entity(model='cube', collider='box', texture='img/Tile-Blank', position=(x,y,z), scale=(1,1,1), enable=True, on_click=get_point)
            else:
                cubes[(x,y,z)] = Entity(model='cube', collider='box', texture='img/Tile-Blank', position=(x,y,z), scale=(1,1,1), enable=True, on_click=get_point)



ec = EditorCamera()
Sky(texture='background')
