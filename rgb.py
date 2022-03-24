# Henry Heisig (hheisig51)
# 2022-03-11
# RGB Library
# Assistance from Karl Helmstetter (helmstk1)

# Importing libraries
import time
import board
import pwmio


class LED:
    '''A class that enables an LED To fade, turn on, and turn off.'''

    def __init__(self, Pin):
        self.LED = pwmio.PWMOut(Pin, frequency=5000, duty_cycle=0)

    def fade(self):
        for i in range(100):
            # PWM LED up and down
            if i < 50:
                self.LED.duty_cycle = int(i * 2 * 65535 / 100)  # Up
            else:
                self.LED.duty_cycle = 65535 - \
                    int((i - 50) * 2 * 65535 / 100)  # Down
            print(self.LED.duty_cycle)
            time.sleep(0.03)

    def on(self, brightness=65535):
        self.LED.duty_cycle = 65535 - brightness

    def off(self):
        self.LED.duty_cycle = 65535
