# Henry Heisig (hheisig51)
# 2022-03-11
# LED Function
#

import board
from rgb import LED

RedPin = board.D5
GreenPin = board.D6
BluePin = board.D7

R = LED(RedPin)
G = LED(GreenPin)
B = LED(BluePin)

while True:
    R.fade()
    G.on(15000)
    B.off()
