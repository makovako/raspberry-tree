"""
Cycle true hue and change brightness per color.
"""
from tree import RGBXmasTree
from colorzero import Color, Hue
from time import sleep

tree = RGBXmasTree()
color = Color('red')
dim = [0.1,0.2,0.3,0.4,0.5]

try:
    while True:
        color += Hue(deg=5)
        tree.color = Color(color)
        for d in dim:
            tree.brightness = d
            sleep(0.5)
        for d in dim[::-1]:
            tree.brightness = d
            sleep(0.5)
except KeyboardInterrupt:
    tree.off()
    tree.close()
    
