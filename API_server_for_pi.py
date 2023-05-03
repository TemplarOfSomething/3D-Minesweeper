from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel

gpio_list = []
led_value = {}
app = FastAPI()

#GPIO
@app.post("/GPIO_Post/")
async def post_gpio(name: str, value: bool):
    gpio_list.append(name)
    gpio_list.append(value)
    return {
        "name":name,
        "value":value
    }

@app.get("/GPIO_Get/")
async def get_gpio(name: str):
    try:
        return gpio_list[int(gpio_list.index(name)) + 1]
    except ValueError:
        return "Value does not exist"

#LED
@app.post("/LED_Post/")
async def post_led(value):
    led_value["value"] = value
    return {
        "value":value
    }

@app.get("/LED_Get/")
async def get_led():
    return led_value["value"]