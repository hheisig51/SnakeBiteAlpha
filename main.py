# Henry Heisig (hheisig51)
# 2022-03-24
# RGB LED code
# Borrowed from Karl Helmstetter (helmstk1), modified by Henry Heisig (hheisig51)

"""This document uses the rgb.py class to make flashing two RGB LEDs simple."""

import time
import board
from rgb import RGB

r1 = board.D8
b1 = board.D9
g1 = board.D10
r2 = board.D4
b2 = board.D7
g2 = board.D5

full = 65535
half = int(65535 / 2)

myRGBled1 = RGB(r1, g1, b1)
myRGBled2 = RGB(r2, g2, b2)

myRGBled1.off()
myRGBled2.off()

while True:
    """Flashes the two LEDs various colors, then has them blink on and off"""
    myRGBled1.blue(half)
    myRGBled2.yellow(half)
    time.sleep(1)
    myRGBled1.off()
    myRGBled2.off()
    time.sleep(2)

    myRGBled1.red()
    myRGBled2.cyan()
    time.sleep(1)
    myRGBled1.off()
    myRGBled2.off()
    time.sleep(2)

    myRGBled1.green()
    myRGBled2.magenta()
    time.sleep(1)
    myRGBled1.off()
    myRGBled2.off()
    time.sleep(2)

    myRGBled1.Blinky(2, 5)
    myRGBled2.Blinky(4, 5)
