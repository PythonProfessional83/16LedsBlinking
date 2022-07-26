# Randomly_3_Blink.py
'''
Module for 3 leds blinking randomly from 16 available leds.
'''
import random
import time
import RPi.GPIO as GPIO
from simple_colors import *


# setting gloabals
GPIOS = [17, 5, 26, 18, 23, 4, 27, 22, 6, 13, 24, 25, 8, 7, 12, 16]
INDEXES = [x for x in range(len(GPIOS))]

def randomly_3_blink(tim_e):
    print(
        red('Enter only "control+c" to finish properly the program!', ['bold']))

    # setting the mode for GPIO
    GPIO.setmode(GPIO.BCM)

    try:
        while True:
            inde_x1 = random.randrange(len(INDEXES))
            inde_x2 = random.randrange(len(INDEXES))
            inde_x3 = random.randrange(len(INDEXES))
            # Setting random GPIO nr from 16 GPIOS avaialble

            if inde_x1 != inde_x2 and inde_x1 != inde_x3 and inde_x2 != inde_x3:
                pin1 = GPIOS[inde_x1]
                pin2 = GPIOS[inde_x2]
                pin3 = GPIOS[inde_x3]
                # setup rundom GOIO nr
            GPIO.setup((pin1, pin2, pin3), GPIO.OUT)

            # led on
            GPIO.output((pin1, pin2, pin3), GPIO.HIGH)
            time.sleep(tim_e)
            # led off
            GPIO.output((pin1, pin2, pin3), GPIO.LOW)
            time.sleep(tim_e)

    except KeyboardInterrupt:
        GPIO.cleanup()


