"""
Cycle around the tree. Does something but not pretty as expected.
"""
from tree import RGBXmasTree
from colorzero import Color
import random

tree = RGBXmasTree()

colors = ['red','yellow','orange','lime','green','aqua','blue','purple','brown']

bottom = [0,6,7,12,15,16,19,24]
bottom = [0,7,19,24,12,6,15,16]
middle = [1,5,8,11,14,17,20,23]
middle = [1,8,20,23,11,5,14,17]
top = [2,4,9,10,13,18,21,22]
top = [2,9,21,22,10,4,13,18]
star = [3]
pixels = bottom + middle + top + star

try:
    tree.brightness = 0.1
    while True:
        color = random.choice(colors)
        for i in range(len(pixels)):
            tree[pixels[i-2]].color = Color('black')
            tree[pixels[i-3]].color = Color('black')
            tree[pixels[i-1]].color = Color(color)
            tree[pixels[i]].color = Color(color)
except KeyboardInterrupt:
    tree.off()
    tree.close()

