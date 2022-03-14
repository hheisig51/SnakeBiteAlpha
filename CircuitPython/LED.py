# Henry Heisig (hheisig51)
# 2022-03-11
# LED Function
#

import board
from rgb import LED

R = board.D5
G = board.D6
B = board.D7

RGB_1 = LED(R, G, B)

RGB_1.test()
