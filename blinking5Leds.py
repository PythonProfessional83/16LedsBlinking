# blinking5Leds.py
'''
In this program 5 leds connected to respberry pi 4b wil be blinking.
'''
import RPi.GPIO as GPIO
import time
from simple_colors import *


# set sentinel
# yes = 'y'

# # infinite loop
# while yes.lower() == 'y':

#     if yes.lower() == 'y':

#         try:
#             tim_e = float(
#                 input('Enter ner time in seconds (format: 0.25): '))
#             # activate function
#             blink(tim_e)
#         except ValueError:
#             pass

#     print()

#     # set sentinel
#     yes = input(
#         "Enter 'y' if you want to enter new time for blinking or press 'n' to finish: ")

# print()
# print('Program is finished.')


def blink5(tim_e):

    # GPIO's PINS
    LED_PIN1 = 17
    LED_PIN2 = 5
    LED_PIN3 = 26
    LED_PIN4 = 18
    LED_PIN5 = 23

    # stup() must be runned only one time not to give an error
    # refer to the GPIO connections
    GPIO.setmode(GPIO.BCM)

    # setup out pins!
    GPIO.setup((LED_PIN1, LED_PIN2, LED_PIN3, LED_PIN4, LED_PIN5), GPIO.OUT)
    print(
        red('Enter only control+c to finish properly the program.', ['bold']))
    print()

    try:
        while True:
            # leds on
            GPIO.output((LED_PIN1, LED_PIN2, LED_PIN3,
                        LED_PIN4, LED_PIN5), GPIO.HIGH)
            time.sleep(tim_e)

            # leds off
            GPIO.output((LED_PIN1, LED_PIN2, LED_PIN3,
                        LED_PIN4, LED_PIN5), GPIO.LOW)
            time.sleep(tim_e)

    # control + c - to rise excpetion
    except KeyboardInterrupt:
        # clear previus gpio's pins settings to be aple to start program again
        GPIO.cleanup()
