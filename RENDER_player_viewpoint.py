from ursina import *
import RENDER_layer_mode

camera.position = (2,2)

def camera_control():
    enable_2d = RENDER_layer_mode.enable_2d
    camera.z += held_keys['w'] * 10 * time.dt
    camera.z -= held_keys['s'] * 10 * time.dt

    camera.x -= held_keys['a'] * 10 * time.dt
    camera.x += held_keys['d'] * 10 * time.dt  

    camera.rotation_y += held_keys['right arrow'] * 30 * time.dt 
    camera.rotation_y -= held_keys['left arrow'] * 30 * time.dt

    if enable_2d == False:
        camera.y += held_keys['up arrow'] * 10 * time.dt 
        camera.rotation_x += held_keys['up arrow'] * 35 * time.dt 

        camera.y -= held_keys['down arrow'] * 10 * time.dt 
        camera.rotation_x -= held_keys['down arrow'] * 35 * time.dt 

