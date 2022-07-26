# blinking1Leds.py
'''
Module for 1 led blinking.
'''
import time
import RPi.GPIO as GPIO
from simple_colors import *


# setting gloabals
GPIOS = [17, 5, 26, 18, 23]
INDEXES = [x for x in range(len(GPIOS))]

# print(f'number of indexes including digit 0: {(len(INDEXES)-1)}')


def blink1(tim_e):

    tex = 'Chosse the GPIO number:'
    print(green(tex, ['bold']))
    print(green(len(tex)*'=', ['bold']))
    print()
    print(blue('0.GPIO17.', ['bold']))
    print(blue('1.GPIO5', ['bold']))
    print(cyan('2.GPIO26', ['bold']))
    print(blue('3.GPIO18', ['bold']))
    print(blue('4.GPIO2', ['bold']))

    yes = 'y'
    while yes.lower() == 'y':

        led = int(
            input(f'Enter GPIO number from list{INDEXES} to let the led start blinking: '))

        # to enter correct led's number
        while led < 0 or led > 4:
            led = int(
                input(f'Enter correct number from the list:\n({INDEXES}): '))

        # setting GPIO nr
        pin = GPIOS[led]

        # setting the mode only one time
        GPIO.setmode(GPIO.BCM)

        print(red('Enter only "control+c" to finish properly the program!', ['bold']))

        while True:
            try:
                # setup GPIO nr
                GPIO.setup(pin, GPIO.OUT)
                # led on
                GPIO.output(pin, GPIO.HIGH)
                time.sleep(tim_e)

                # led off
                GPIO.output(pin, GPIO.LOW)
                time.sleep(tim_e)
            except KeyboardInterrupt:

                GPIO.cleanup()
