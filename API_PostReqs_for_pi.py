import requests
from internetinfo import *

POST_URL = f"http://{IP}:{PORT}/GPIO_Post/"       #replace with ip and port from pi, since it hosts
GET_URL = f"http://{IP}:{PORT}/LED_Get/"
PUT_URL = f"http://{IP}:{PORT}/GPIO_Put"

#format used for both buttons
#requests.post(url=POST_URL, data={"name":"gpio{number}", "value":False})    #false by default

#used to get LED value
#requests.get(url=GET_URL)

#used to put (UPDATE) values for buttons
#requests.put(url=PUT_URL, data={"name":"gpio{number}", "value":False})