# blink_10_leds.py
'''
In this program 10 leds connected to respberry pi 4b wil be blinking
simultaneously.
'''
import RPi.GPIO as GPIO
import time
from simple_colors import *


def blink10(tim_e):

    # GPIO's PINS
    LED_PIN1 = 17
    LED_PIN2 = 5
    LED_PIN3 = 26
    LED_PIN4 = 18
    LED_PIN5 = 23
    PIN6 = 4
    PIN7 = 27
    PIN8 = 22
    PIN9 = 6
    PIN10 = 13
    PIN11 = 24
    PIN12 = 25
    PIN13 = 8
    PIN14 = 7
    PIN15 = 12
    PIN16 = 16

    # stup() must be runned only one time not to give an error
    # refer to the GPIO connections
    GPIO.setmode(GPIO.BCM)

    # setup out pins!
    GPIO.setup((LED_PIN1, LED_PIN2, LED_PIN3, LED_PIN4, LED_PIN5,
                PIN6, PIN7, PIN8, PIN9, PIN10, PIN11, PIN12, PIN13,
                PIN14, PIN15, PIN16), GPIO.OUT)
    print(
        red('Enter only control+c to finish properly the program.', ['bold']))
    print()

    try:
        while True:
            # leds on
            GPIO.output((LED_PIN1, LED_PIN2, LED_PIN3,
                        LED_PIN4, LED_PIN5, PIN6, PIN7, PIN8, PIN9, PIN10, PIN11,
                        PIN12, PIN13, PIN14, PIN15, PIN16), GPIO.HIGH)
            time.sleep(tim_e)

            # leds off
            GPIO.output((LED_PIN1, LED_PIN2, LED_PIN3,
                        LED_PIN4, LED_PIN5, PIN6, PIN7, PIN8, PIN9, PIN10, PIN11,
                        PIN12, PIN13, PIN14, PIN15, PIN16), GPIO.LOW)
            time.sleep(tim_e)

    # control + c - to rise excpetion
    except KeyboardInterrupt:
        # clear previus gpio's pins settings to be aple to start program again
        GPIO.cleanup()
