import RPi.GPIO as GPIO
from time import sleep
from API_PostReqs_for_pi import *
from API_PostReqs_for_PC import POST_LED_URL

#GPIO setup
GPIO.setmode(GPIO.BCM)

LED_ZERO = 19
LED_ONE = 18
LED_TWO = 17
LED_THREE = 16
LED_FOUR = 13
LED_LIST = [LED_ZERO, LED_ONE, LED_TWO, LED_THREE, LED_FOUR]

BUTTON_ONE = 4
BUTTON_TWO = 5

GPIO.setup(LED_ZERO, GPIO.OUT)
GPIO.setup(LED_ONE, GPIO.OUT)
GPIO.setup(LED_TWO, GPIO.OUT)
GPIO.setup(LED_THREE, GPIO.OUT)
GPIO.setup(LED_FOUR, GPIO.OUT)

GPIO.setup(BUTTON_ONE, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(BUTTON_TWO, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

#API setup
TERMINATION_POST = "http://{ip}:{port}/Terminate_Post/"
TERMINATION_GET = "http://{ip}:{port}/Terminate_Get/"
TERMINATION_PUT = "http://{ip}:{port}/Terminate_Put/"

requests.post(url=POST_URL, params={"name":"BUTTON_ONE", "value":False})
requests.post(url=POST_URL, params={"name":"BUTTON_TWO", "value":False})
requests.post(url=POST_LED_URL, params={"value":False})
requests.post(url=TERMINATION_POST, params={"value":False})

#functions
def put_req(name:str, value:bool):
    return requests.put(url=PUT_URL, params={"name":name, "value":value})

#main

button_one_active = False
button_two_active = False
led_status = False
terminate = False

while True:
    #button one for layer mode
    if GPIO.input(BUTTON_ONE) == GPIO.HIGH and button_one_active == True:
        put_req("BUTTON_ONE", False)
        print("MODE OFF")
        button_one_active = False
        sleep(1)
    if GPIO.input(BUTTON_ONE) == GPIO.HIGH and button_one_active == False:
        put_req("BUTTON_ONE", True)
        print("MODE ON")
        button_one_active = True
        sleep(1)

    #button two for minesweeper mode
    if GPIO.input(BUTTON_TWO) == GPIO.HIGH and button_two_active == True:
        put_req("BUTTON_TWO", False)
        print("2 MODE OFF")
        button_two_active = False
        sleep(1)
    if GPIO.input(BUTTON_TWO) == GPIO.HIGH and button_two_active == False:
        put_req("BUTTON_TWO", True)
        print("2 MODE ON")
        button_two_active = True
        sleep(1)

    #LED
    if button_two_active == True:
        led_status = requests.get(url=GET_URL).json()
        if led_status != "False" or False:                           #json conversion mishap?
            GPIO.output(LED_LIST[led_status],GPIO.HIGH)
        sleep(0.5)
    
    if button_two_active == False:
        if led_status != "False" or False:
            GPIO.output(LED_LIST[led_status], GPIO.LOW)
    
    #Termination
    if requests.get(url=TERMINATION_GET).json() == "True" or True:
        requests.put(url=POST_URL, params={"name":"BUTTON_ONE", "value":False})
        requests.put(url=POST_URL, params={"name":"BUTTON_TWO", "value":False})
        requests.put(url=POST_LED_URL, params={"value":False})
        requests.put(url=TERMINATION_POST, params={"value":False})

        
    

        

