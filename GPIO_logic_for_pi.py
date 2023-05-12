import RPi.GPIO as GPIO
from time import sleep
from API_PostReqs_for_pi import *
from API_PostReqs_for_PC import POST_LED_URL
from internetinfo import *

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
TERMINATION_POST = "http://{}:{}/Terminate_Post/".format(IP, PORT)
TERMINATION_GET = "http://{}:{}/Terminate_Get/".format(IP, PORT)
TERMINATION_PUT = "http://{}:{}/Terminate_Put/".format(IP, PORT)

requests.post(url=POST_URL, params={"name":"BUTTON_ONE", "value":False})
requests.post(url=POST_URL, params={"name":"BUTTON_TWO", "value":False})
requests.post(url=POST_LED_URL, params={"value":False})
requests.post(url=TERMINATION_POST, params={"value":False})

#functions
def put_req(name:str, value:bool):
    return requests.put(url=PUT_URL, params={"name":name, "value":value})

#main


button_one_active = False
led_status = False
terminate = False

while True:
    #button one (layer mode)
    """
    if GPIO.input(BUTTON_ONE) == GPIO.HIGH and button_one_active == True:
        put_req("BUTTON_ONE", False)
        print("MODE_OFF")
        button_one_active = False
        sleep(1)
    """
    if GPIO.input(BUTTON_TWO) == GPIO.HIGH:
        put_req("BUTTON_TWO", True)
        print("MODE ON")
        button_two_active = True
        sleep(1)

    #button two (minesweeper mode)
    if GPIO.input(BUTTON_ONE) == GPIO.HIGH and button_two_active == True:
        put_req("BUTTON_ONE", False)
        print("MODE_OFF")
        button_one_active = False
        sleep(1)
    
    if GPIO.input(BUTTON_ONE) == GPIO.HIGH and button_two_active == False:
        put_req("BUTTON_ONE", True)
        print("2 MODE ON")
        button_one_active = True
        sleep(1)

    #LED
    if button_one_active == True:
        led_status = requests.get(url=GET_URL).json()
        prev_led = led_status
        if led_status != False:                           #json conversion mishap?
            GPIO.output(LED_LIST[-int(led_status)],GPIO.HIGH)
        sleep(0.5)
    
    if button_one_active == False:
            GPIO.output(LED_LIST[-int(led_status)], GPIO.LOW)
    
    #Termination
    if requests.get(url=TERMINATION_GET).json() == True:
        requests.put(url=POST_URL, params={"name":"BUTTON_ONE", "value":False})
        requests.put(url=POST_URL, params={"name":"BUTTON_TWO", "value":False})
        requests.put(url=POST_LED_URL, params={"value":False})
        requests.put(url=TERMINATION_POST, params={"value":False})
        button_one_active = False
        led_status = False
        terminate = False
    sleep(1)
    #print(requests.get(url="http://{IP}:{}/GPIO_Get/", params={"name":"BUTTON_ONE"}).json()) #testing

        
    

        

