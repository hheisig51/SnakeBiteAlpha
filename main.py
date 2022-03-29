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

runtime = 3

"""
runtime_1: blinky test (ln 35)
runtime_2: show-off (ln 41)
runtime_3: colors test (ln 77)
"""

while runtime == 0:
    """Testing blinky function"""
    myRGBled1.blinky(.1, 50)
    myRGBled2.off()


while runtime == 1:
    """Flashes the two LEDs various colors, then has them blink on and off"""
    print(f"Starting blue-yellow")
    myRGBled1.blue(half)
    myRGBled2.yellow(half)
    time.sleep(1)
    myRGBled1.off()
    myRGBled2.off()
    time.sleep(1)
    print(f"Finished blue-yellow\n")

    print(f"Starting red-cyan")
    myRGBled1.red()
    myRGBled2.cyan()
    time.sleep(1)
    myRGBled1.off()
    myRGBled2.off()
    time.sleep(1)
    print(f"Finished red-cyan\n")

    print(f"Starting green-magenta")
    myRGBled1.green()
    myRGBled2.magenta()
    time.sleep(1)
    myRGBled1.off()
    myRGBled2.off()
    time.sleep(1)
    print(f"Finished green-magenta\n")

    print(f"Starting blinky")
    myRGBled1.blinky(.5, 50)
    myRGBled2.blinky(.1, 50)
    time.sleep(4)
    print(f"Finished blinky\n")

while runtime == 3:
    myRGBled1.white()
    myRGBled2.magenta()