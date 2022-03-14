# Henry Heisig (hheisig51)
# 2022-03-11
# RGB Library
#

# Importing libraries
import time
import board
import pwmio
import digitalio

class LED:
    """PLACEHOLDER"""

    def __init__(self, RedPin, GreenPin, BluePin):
        self.RedPin = RedPin
        self.GreenPin = GreenPin
        self.BluePin = BluePin
        self.RedPin = pwmio.PWMOut(RedPin, frequency=5000, duty_cycle=65535)
        self.GreenPin = pwmio.PWMOut(GreenPin, frequency=5000, duty_cycle=65535)
        self.BluePin = pwmio.PWMOut(BluePin, frequency=5000, duty_cycle=65535)

    def test(self):
        self.color((255, 0, 0))
        print(f"please let this work")
