from ursina import *
import RENDER_minefield_rendering
import MATH_blank_logic
from time import sleep
from MATH_minefield_logic import limited_minefield_dict as logic

# Set up variables needed from imported files

cubes = RENDER_minefield_rendering.cubes
mine_dict = RENDER_minefield_rendering.mine_dict
clicked = RENDER_minefield_rendering.clicked

# Waits for left or right click

def update():
    global blank_chain
    if mouse.left == True:
        blank_chain = MATH_blank_logic.blank_chain_revealer(mine_dict, RENDER_minefield_rendering.round_point())
        show_numbers()
        sleep(0.5)

    if mouse.right == True:
        mouse.hovered_entity.color = color.orange

# Rus through and destroys/reveals connected mines

def show_numbers():
    global cubes
    global blank_chain
    for z in range(5):
        for y in range(5):
            for x in range(5):
                try: 
                    if RENDER_minefield_rendering.cubes[(x,y,z)].color == color.orange:
                        pass
                    else:
                        if blank_chain[(x,y,z)] == 0:
                            destroy(RENDER_minefield_rendering.cubes[(x,y,z)])
                        elif blank_chain[(x,y,z)] == 1:
                            RENDER_minefield_rendering.cubes[(x,y,z)].texture = 'img/Tile-1'
                        elif blank_chain[(x,y,z)] == 2:
                            RENDER_minefield_rendering.cubes[(x,y,z)].texture = 'img/Tile-2'
                        elif blank_chain[(x,y,z)] == 3:
                            RENDER_minefield_rendering.cubes[(x,y,z)].texture = 'img/Tile-3'
                        elif blank_chain[(x,y,z)] == 4:
                            RENDER_minefield_rendering.cubes[(x,y,z)].texture = 'img/Tile-4'
                        elif blank_chain[(x,y,z)] == 5:
                            RENDER_minefield_rendering.cubes[(x,y,z)].texture = 'img/Tile-5'
                        elif blank_chain[(x,y,z)] == 6:
                            RENDER_minefield_rendering.cubes[(x,y,z)].texture = 'img/Tile-6'
                        elif blank_chain[(x,y,z)] == 7:
                            RENDER_minefield_rendering.cubes[(x,y,z)].texture = 'img/Tile-7'
                        elif blank_chain[(x,y,z)] == 8:
                            RENDER_minefield_rendering.cubes[(x,y,z)].texture = 'img/Tile-8'
                        elif blank_chain[(x,y,z)] == '*':
                            pass
                except KeyError:
                    pass

