# Henry Heisig (hheisig51)
# 2022-03-11
# RGB Library
#

# Importing libraries
import time
import board
import pwmio


class LED:
    """PLACEHOLDER"""

    def __init__(self, RedPin, GreenPin, BluePin):
        self.RedPin = RedPin
        self.GreenPin = GreenPin
        self.BluePin = BluePin

    def test(self):
        self.color((255, 0, 0))
        print(f"please let this work")
