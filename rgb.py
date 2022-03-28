# Henry Heisig (hheisig51)
# 2022-03-24
# RGB LED code
# Borrowed from Karl Helmstetter (helmstk1), modified by Henry Heisig (hheisig51)

import time
import board
import pwmio
import digitalio

lightBulb = digitalio.DigitalInOut(board.D13)
lightBulb.direction = digitalio.Direction.OUTPUT


class LED:
    def __init__(self, ledpin, name):

        self.led = pwmio.PWMOut(ledpin, frequency=5000, duty_cycle=0)
        self.name = name

    def fadedown(self):
        for i in range(255):
            if i < (255 / 2):
                self.led.duty_cycle = int(i * 65535 / (255 / 2))
            print(self.name, ", ", self.led.duty_cycle)
            time.sleep(0.01)

    def fadeup(self):
        for i in range(255):
            if i > (255 / 2):
                self.led.duty_cycle = 65535 - int((i - (255 / 2)) * 65535 / (255 / 2))
            print(self.name, ", ", self.led.duty_cycle)
            time.sleep(0.01)

    def on(self, brightness=65535):
        self.led.duty_cycle = 65535 - brightness
        lightBulb.value = 65535

    def off(self):
        self.led.duty_cycle = 65535

    def half(self, brightness=65535):
        self.led.duty_cycle = int(65535 / 2)


class RGB:

    from rgb import LED

    def __init__(self, redPin, greenPin, bluePin):
        self.myRedLED = LED(redPin, "red")
        self.myBlueLED = LED(bluePin, "blue")
        self.myGreenLED = LED(greenPin, "green")

    def blue(self, brightness=65535):
        self.myBlueLED.on(brightness)
        self.myGreenLED.off()
        self.myRedLED.off()

    def yellow(self, brightess=65535):
        self.myRedLED.on()
        self.myGreenLED.on()
        self.myBlueLED.off()

    def red(self, brightness=65535):
        self.myRedLED.on()
        self.myGreenLED.off()
        self.myBlueLED.off()

    def cyan(self, brightness=65535):
        self.myRedLED.off()
        self.myGreenLED.half()
        self.myBlueLED.on()

    def green(self, brightness=65535):
        self.myRedLED.off()
        self.myGreenLED.on()
        self.myBlueLED.off()

    def magenta(self, brightness=65535):
        self.myRedLED.on()
        self.myGreenLED.off()
        self.myBlueLED.on()

    def Blinky(self, t, l):
        for l in range(l, 0):
            print(f"Rate: {t} seconds\n Cycles left: {l}")
            self.myRedLED.on()
            self.myGreenLED.on()
            self.myBlueLED.on()
            time.sleep(t)
            self.myRedLED.off()
            self.myGreenLED.off()
            self.myBlueLED.off()
            time.sleep(t)
            if l == 0:
                break

    def off(self):
        self.myBlueLED.off()
        self.myGreenLED.off()
        self.myRedLED.off()
        lightBulb.value = 0
