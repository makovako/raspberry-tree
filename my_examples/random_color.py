"""
Pick a random led and put a random color on it.
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
        random.choice(tree).color = Color(random.choice(color))
        random.choice(tree).color = Color(random.choice(color))
        random.choice(tree).color = Color(random.choice(color))
        random.choice(tree).color = Color(random.choice(color))
        random.choice(tree).color = Color(random.choice(color))
        #sleep(0.3)
except KeyboardInterrupt:
    tree.off()
    tree.close()
