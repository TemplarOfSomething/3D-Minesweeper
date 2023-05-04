
from fastapi import FastAPI

gpio_list = []
led_value = {}
terminate = False
app = FastAPI()

#test
@app.get("/")
async def test_server():
    return {"message":"Hello Word"}


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

@app.put("/GPIO_Put/")
async def put_gpio(name:str, value:bool):
    gpio_list[int(gpio_list.index(name)) + 1] = value
    return gpio_list[int(gpio_list.index(name)) + 1]
    
#LED
@app.post("/LED_Post/")
async def post_led(value):
    led_value["value"] = value
    return {
        "value":value
    }

@app.get("/LED_Get/")
async def get_led():
    return led_value.get("value")

@app.put("/LED_Put/")
async def put_led(value):
    led_value["value"] = value
    return {
        "value":value
    }

#Termination
@app.post("/Terminate_Post/")
async def post_termination(value:bool):
    terminate = value
    return {
        "value":value
    }

@app.get("/Terminate_Get/")
async def get_termination():
    return terminate

@app.put("/Terminate_Put/")
async def put_termination(value:bool):
    terminate = value
    return {
        "value":value
    }