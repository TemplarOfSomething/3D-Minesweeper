import requests

POST_URL = "http:{ip}:{port}/LED_POST/"       #replace with ip and port from pi, since it hosts
GET_URL = "http:{ip}:{port}/GPIO_GET/"

#post led
requests.post(url=POST_URL, data={"value":value})

#get gpio
requests.get(url=GET_URL, params="{GPIO#}")