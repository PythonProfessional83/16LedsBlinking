# menu.py
'''
Cho0sing light for blinking and activation proper function.
'''

from blinking1Leds import blink1
from blinking5Leds import blink5
from blink_10_leds import blink10

from Randomly_1_Blink import randomly_1_blink
from Randomly_2_Blink import randomly_2_blink
from Randomly_3_Blink import randomly_3_blink
from Randomly_4_Blink import randomly_4_blink
from Randomly_5_Blink import randomly_5_blink
from Randomly_6_Blink import randomly_6_blink
from Randomly_7_Blink import randomly_7_blink

from simple_colors import *

# yellow(self.domain,['bold'])
# global constants

# 1 led blinking simaltenously
BLINK_1_LEDS = 1

# 5 leds blinking
BLINK_5_LEDS = 2

# 10 leds blinking
BLINK_10_LEDS = 3

# blinking 1 led randomly
RANDOMLY_1_LEDS = 4

# blinking 2 leds randomly
RANDOMLY_2_LEDS = 5

# blinking 3 leds randomly
RANDOMLY_3_LEDS = 6

# blinking 4 leds randomly
RANDOMLY_4_LEDS = 7

# blinking 5 leds randomly
RANDOMLY_5_LEDS = 8

# blinking 6 leds randomly
RANDOMLY_6_LEDS = 9

# blinking 7 leds randomly
RANDOMLY_7_LEDS = 10


# Quit the program
QUIT = 21


def main():
    # initialization of variable choice

    # returning choice nr
    choice = menu()

    while choice != QUIT:

        # choosing imported method from corresponding file file

        # set the time for blinking
        fla_g = True

        try:
            while fla_g:

                try:
                    tim_e = float(
                        input(cyan('Enter the time in format (0.25): ', ['bold'])))
                    fla_g = False
                except ValueError:
                    print(red('Enter the time in correct format', ['bold']))

        # activation the outer module
            flag = True
            while flag:
                try:
                    if choice == BLINK_1_LEDS:
                        blink1(tim_e)
                        flag = False

                    elif choice == BLINK_5_LEDS:
                        blink5(tim_e)
                        flag = False

                    elif choice == BLINK_10_LEDS:
                        blink10(tim_e)
                        flag = False

                    elif choice == RANDOMLY_1_LEDS:
                        randomly_1_blink(tim_e)
                        flag = False

                    elif choice == RANDOMLY_2_LEDS:
                        randomly_2_blink((tim_e))
                        flag = False

                    elif choice == RANDOMLY_3_LEDS:
                        randomly_3_blink(tim_e)
                        flag = False

                    elif choice == RANDOMLY_4_LEDS:
                        randomly_4_blink(tim_e)
                        flag = False

                    elif choice == RANDOMLY_5_LEDS:
                        randomly_5_blink(tim_e)
                        flag = False

                    elif choice == RANDOMLY_6_LEDS:
                        randomly_6_blink(tim_e)
                        flag = False

                    elif choice == RANDOMLY_7_LEDS:
                        randomly_7_blink(tim_e)
                        flag = False

                except UnboundLocalError:
                    pass

        except RuntimeError:
            pass

        choice = menu()

    print(red('Program is finished! Bye, Bye!', ['bold']))


def menu():
    tex = 'Raspberry PI Leds Menu'
    print(green(tex, ['bold']))
    print(green(len(tex)*'=', ['bold']))
    print()

    print(blue('1.One led blinking.', ['bold']))
    print(blue('2.Five leds blinking simultanously.', ['bold']))
    print(blue('3.Sixteen leds blinking simultanously.', ['bold']))
    print()

    print(cyan('4.One led blinking randomly.', ['bold']))
    print(cyan('5.Two leds blinking together randomly.', ['bold']))
    print(cyan('6.Three leds blinking together randomly.', ['bold']))
    print(cyan('7.Four leds blinking together randomly.', ['bold']))
    print(cyan('8.Five leds blinking together randomly.', ['bold']))
    print(cyan('9.Six leds blinking together randomly.', ['bold']))
    print(cyan('10.Seven leds blinking together randomly.', ['bold']))

    print()
    print(red('21.Quit', ['bold']))

    flag = True

    while flag:
        try:
            choice = int(input(magenta('Etner you choice nr: ', 'underlined')))
            flag = False
        except ValueError:
            pass

    # security for choice nr
    while choice < BLINK_1_LEDS or choice > QUIT:
        try:
            choice = int(input(red('Etner your choice nr: ', ['bold'])))
        except ValueError:
            pass

    return choice


main()
