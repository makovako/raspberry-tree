"""
Pick a random color and dim via brigness levels.
"""
from tree import RGBXmasTree
import random
from colorzero import Color

colors = ['red','yellow','orange','lime','green','aqua','blue','purple','brown']

dim = [0,0.1,0.2,0.3,0.5]

tree = RGBXmasTree()

try:
    while True:
        color = random.choice(colors)
        tree.color = Color(color)
        for d in dim:
            tree.brightness = d
        for d in dim[::-1]:
            tree.brightness = d
except KeyboardInterrupt:
    tree.off()
    tree.close()
