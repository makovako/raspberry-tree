"""
Cycle betwwen different colors (through black/off)
"""
from tree import RGBXmasTree
import random
from time import sleep
from colorzero import Color

tree = RGBXmasTree()
tree.brightness = 0.1

color = ['red','yellow','orange','lime','green','aqua','blue','purple','brown']

try:
    while True:
        tree.color = Color(random.choice(color))
        #sleep(0.5)
        tree.color = Color('black')
        #sleep(0.5)
except KeyboardInterrupt:
    tree.off()
    tree.close()
