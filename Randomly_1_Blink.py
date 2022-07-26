'''
Module for 1 led blinking randomly from 16 available leds.
'''
import random
import time
import RPi.GPIO as GPIO
from simple_colors import *


# setting gloabals
GPIOS = [17, 5, 26, 18, 23, 4, 27, 22, 6, 13, 24, 25, 8, 7, 12, 16]
INDEXES = [x for x in range(len(GPIOS))]


def randomly_1_blink(tim_e):
    print(
        red('Enter only "control+c" to finish properly the program!', ['bold']))

    # setting the mode for GPIO
    GPIO.setmode(GPIO.BCM)

    try:
        while True:
            inde_x = random.randrange(len(INDEXES))
            # Setting random GPIO nr from 16 GPIOS avaialble
            pin = GPIOS[inde_x]
            # setup rundom GOIO nr
            GPIO.setup(pin, GPIO.OUT)

            # led on
            GPIO.output(pin, GPIO.HIGH)
            time.sleep(tim_e)
            # led off
            GPIO.output(pin, GPIO.LOW)
            time.sleep(tim_e)

    except KeyboardInterrupt:
        GPIO.cleanup()
