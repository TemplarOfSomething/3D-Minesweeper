import requests
from RENDER_minefield_rendering import app
from API_PostReqs_for_PC import *
from internetinfo import *

#constants
TERMINATION_PUT = f"http://{IP}:{PORT}/Terminate_Put/"

#functions
def get_GPIO(name:str):
    return requests.get(url=GET_URL, params={"name":name}).json()
def put_LED(value):
    return requests.put(url=PUT_URL, params={"value":value}).json()
def put_TERMINATION(value:bool):
    return requests.put(url=TERMINATION_PUT, params={"value":value}).json()

        

