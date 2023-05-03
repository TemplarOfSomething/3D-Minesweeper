import requests

POST_URL = "http:{ip}:{port}/LED_POST/"       #replace with ip and port from pi, since it hosts
GET_URL = "http:{ip}:{port}/GPIO_GET/"
PUT_URL = "http:{ip}:{post}/LED_PUT/"

#post led
requests.post(url=POST_URL, data={"value":value})

#get gpio
requests.get(url=GET_URL, params="{GPIO#}")

#put (UPDATE) led
requests.put(url=PUT_URL, data={"value":value})