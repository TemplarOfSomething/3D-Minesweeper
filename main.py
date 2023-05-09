#hopefully this will be the main file for the game (with it being called "main.py" and all)

from ursina import *
from RENDER_minefield_rendering import *
from RENDER_layer_mode import *
from RENDER_minefield_rendering import app
from RENDER_clicking_logic import *
from RENDER_player_viewpoint import *
from GPIO_PC_Integration import *
#app.run()
while True:
    app.step()
    sleep(0.01)     #mock framerate






