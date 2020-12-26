"""
Cycle trough red and yellow (or any other) color.
"""
from tree import RGBXmasTree
import random
from time import sleep
from colorzero import Color

tree = RGBXmasTree()
tree.brightness = 0.1

color = ['red','yellow','orange','lime','green','aqua','blue','purple','brown']

# Just a boolean to determine in which part of 2 cycle am I
lala = True
try:
    while True:
        # value is list of 25 triplets of rgb values 
        if lala:
            value = [Color('red') if i%2 == 0 else Color('yellow') for i in range(25) ]
            #tree.value = [Color(random.choice(color)) for _ in range(25)]
        else:
            #tree.value = [Color(random.choice(color)) for _ in range(25)]
            value = [Color('yellow') if i%2 == 0 else Color('red') for i in range(25) ]
            #value = [Color('lime') if i%2 == 0 else Color('blue') for i in range(25) ]
        tree.value = value
        #sleep(0.5)
        # Uncomment to turn it off between cycles
        #tree.value = [(0,0,0)] * 25
        #sleep(0.5)
        lala = not lala
except KeyboardInterrupt:
    tree.off()
    tree.close()
