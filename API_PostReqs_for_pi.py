import requests

POST_URL = "http:{ip}:{port}/GPIO_POST/"       #replace with ip and port from pi, since it hosts
GET_URL = "http:{ip}:{port}/LED_GET/"

#format used for both buttons
requests.post(url=POST_URL, data={"name":"gpio{number}", "value":False})    #false by default

#used to get LED value
requests.get(url=GET_URL)