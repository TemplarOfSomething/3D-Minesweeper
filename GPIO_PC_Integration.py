import requests
from RENDER_layer_mode import *
from API_PostReqs_for_PC import *
from time import sleep

#constants
TERMINATION_PUT = "http://{ip}:{port}/Terminate_Put/"

#functions
def get_GPIO(name:str):
    requests.get(url=GET_URL, params={"name":name}).json()
def put_LED(value):
    requests.put(url=PUT_URL, params={"value":value}).json()
def put_TERMINATION(value:bool):
    requests.put(url=TERMINATION_PUT, params={"value":value}).json()

while True:
    #one is layer mode, two is sweep mode
    button_one = get_GPIO("BUTTON_ONE")
    button_two = get_GPIO("BUTTON_TWO")

    if button_one == "True" or True:        #double checking due to json conversion
        if enable_2d:
            back_to_3d()
            enable_2d = False
        else:
            proper_list = proper_list_func(mine_list)
            proper_dict(cubes, proper_list)
            enable_2d = True
        
    if button_two == "True" or True:
        pass

    sleep(1)

