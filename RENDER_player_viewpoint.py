from ursina import *

camera.position = (2,2)
def update():
    camera_control()

def camera_control():
    camera.z += held_keys['w'] * 10 * time.dt
    camera.z -= held_keys['s'] * 10 * time.dt

    camera.x -= held_keys['a'] * 10 * time.dt
    camera.x += held_keys['d'] * 10 * time.dt 

    camera.rotation_y += held_keys['z'] * 30 * time.dt 
    camera.rotation_y -= held_keys['x'] * 30 * time.dt

    camera.y += held_keys['f'] * 10 * time.dt 
    camera.rotation_x += held_keys['f'] * 35 * time.dt 

    camera.y -= held_keys['c'] * 10 * time.dt 
    camera.rotation_x -= held_keys['c'] * 35 * time.dt 

