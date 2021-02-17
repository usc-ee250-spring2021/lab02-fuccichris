""" EE 250L Lab 02: GrovePi Sensors

List team members here. None (received lab kit late)

Insert Github repository link here.
Link: https://github.com/usc-ee250-spring2021/lab02-fuccichris/tree/lab02
"""

"""python3 interpreters in Ubuntu (and other linux distros) will look in a 
default set of directories for modules when a program tries to `import` one. 
Examples of some default directories are (but not limited to):
  /usr/lib/python3.5
  /usr/local/lib/python3.5/dist-packages

The `sys` module, however, is a builtin that is written in and compiled in C for
performance. Because of this, you will not find this in the default directories.
"""
import sys
import time
# By appending the folder of all the GrovePi libraries to the system path here,
# we are successfully `import grovepi`
sys.path.append('../../GrovePi/Software/Python/')
# This append is to support importing the LCD library.
sys.path.append('../../GrovePi/Software/Python/grove_rgb_lcd')

import grovepi
from grove_rgb_lcd import *

"""This if-statement checks if you are running this python file directly. That 
is, if you run `python3 grovepi_sensors.py` in terminal, this if-statement will 
be true"""
if __name__ == '__main__':
    PORT = 4    # D4
    potentiometer = 2 #A2
    setText("")
    while True:
        #So we do not poll the sensors too quickly which may introduce noise,
        #sleep for a reasonable time of 200ms between each iteration.
        time.sleep(0.2)
        
        #Measures current distance
        currentDist = grovepi.ultrasonicRead(PORT)

        #Measures threshold
        distance = grovepi.analogRead(potentiometer)
        
        #TODO: print information to screen
        if(currentDist > distance):
            #setRGB_norefresh(255,0,0)
            setText_norefresh(str(distance) + "cm               \n" + str(currentDist) + "cm")
            setRGB(0,255,0)
        else:
            #setRGB_norefresh(0,255,0)
            setText_norefresh(str(distance) + "cm " + "OBJ PRESS\n" + str(currentDist) + "cm")
            setRGB(255,0,0)
        
