from ursina import *
import RENDER_minefield_rendering
import MATH_blank_logic
from time import sleep
from MATH_minefield_logic import limited_minefield_dict as logic

# Set up variables needed from imported files

global already_dead
already_dead = False
cubes = RENDER_minefield_rendering.cubes
mine_dict = RENDER_minefield_rendering.mine_dict
clicked = RENDER_minefield_rendering.clicked

# Waits for left or right click

def update():
    # Brings in all global variables

    global blank_chain
    global already_dead
    global what_happened
    global button

    # Only runs if clicked on an entity
    try:
        # Runs for left click only
        if (mouse.left == True) and (already_dead == False):
            # If entity is a mine, game over
            if mine_dict[RENDER_minefield_rendering.point] == '*':
                death_screen()
                what_happened.text = 'You have hit a mine and died!'
                what_happened.color = color.red
                button = Button(text='EXIT', position=(0,0), color=color.red, text_color=color.black, on_click=exit)
                button.fit_to_text()
            # Else entity is destroyed and surronding mines are shown
            else:
                blank_chain = MATH_blank_logic.blank_chain_revealer(mine_dict, RENDER_minefield_rendering.point)
                show_numbers()
                destroy(mouse.hovered_entity)
                sleep(0.5)
        # Runs for right click only
        if mouse.right == True:
            # Runs if there are no flags left
            if RENDER_minefield_rendering.flag_count > 0:
                mouse.hovered_entity.color = color.orange
                RENDER_minefield_rendering.flag_count -= 1
                RENDER_minefield_rendering.flags.text = RENDER_minefield_rendering.flag_count
                sleep(0.5)
            # If entity is already flagged, removes flag and adds back into count
            elif mouse.hovered_entity.color == color.orange:
                RENDER_minefield_rendering.flag_count += 1
                RENDER_minefield_rendering.flags.text = RENDER_minefield_rendering.flag_count
                mouse.hovered_entity.color = color.white
                sleep(0.5)
            # Flags entity if not already flagged
            else:
                if already_dead == False:
                    death_screen()
                    what_happened.text = 'You are out of flags right now.'
                    button = Button(text='Go_Back', position=(0,0), color=color.green, text_color=color.black, on_click=go_back)
                    button.fit_to_text()
                    already_dead = True
                else:
                    pass
    # If not clicked on entity, nothing happens
    except AttributeError:
        already_dead = False
        sleep(0.5)

# Respawns the minefield

def go_back():
    global back_drop
    global what_happened
    global button
    destroy(back_drop)
    destroy(what_happened)
    destroy(button)
    for z in range(5):
            for y in range(5):
                for x in range(5):
                    RENDER_minefield_rendering.cubes[(x,y,z)].enabled = True
    global already_dead
    already_dead = False
                    

# Hides cubes for the death scene and sets up backdrop

def death_screen():
        global what_happened
        global back_drop
        for z in range(5):
            for y in range(5):
                for x in range(5):
                    RENDER_minefield_rendering.cubes[(x,y,z)].enabled = False
        back_drop = Entity(model='quad', scale=(20,20), enabled=True)
        what_happened = Text(text='', origin=(0,3), color=color.black, enabled=True)

# Rus through and destroys/reveals conne,cted mines

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

