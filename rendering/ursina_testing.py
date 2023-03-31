from ursina import *

e2 = Entity(model='cube', color=(255, 255, 255, 1), rotation=(20, 40, 50))
def my_update_two():
    e2.rotation_y += 20 * time.dt # dt is short for delta time, the duration since the last frame.
    e2.rotation_z += 20 * time.dt # dt is short for delta time, the duration since the last frame.
    e2.rotation_x -= 20 * time.dt # dt is short for delta time, the duration since the last frame.
e2.update = my_update_two

EditorCamera()  #hold right click and use wasd plus mouse movement to look around

Ursina(size=(800, 600), borderless=False).run()