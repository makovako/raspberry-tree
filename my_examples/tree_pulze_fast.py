"""
Pick random color and turn the leds on per level. Bottom -> Middle -> Top -> Star -> and back
"""
from tree import RGBXmasTree
import random
from time import sleep
from colorzero import Color

tree = RGBXmasTree()
tree.brightness = 0.1

colors = ['red','yellow','orange','lime','green','aqua','blue','purple','brown']

# Indexes of leds
bottom = [0,7,19,24,12,6,15,16]
middle = [1,8,20,23,11,5,14,17]
top = [2,9,21,22,10,4,13,18]
star = [3]

def gen_value(color, indexes):
    out = []
    for i in range(25):
        if i in indexes:
            out.append(Color(color))
        else:
            out.append((0,0,0))
    return out

try:
    while True:
        color = random.choice(colors)
        tree.value = gen_value(color, bottom)
        tree.value = gen_value(color, bottom+middle)
        tree.value = gen_value(color, bottom+middle+top)
        tree.value = gen_value(color, bottom+middle+top+star)
        tree.value = gen_value(color, bottom+middle+top)
        tree.value = gen_value(color, bottom+middle)
        tree.value = gen_value(color, bottom)
        tree.value = [(0,0,0)] * 25
except KeyboardInterrupt:
    tree.off()
    tree.close()
