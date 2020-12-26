"""
Pick random color, cycle per layers one led at a time.
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

lala = True

try:
    tree.brightness = 0.1
    while True:
#        if lala:
#            color = [Color('red'),Color('yellow'),Color('orange'),Color('purple')]
#        else:
#            color = [Color('lime'),Color('blue'),Color('green'),Color('aqua')]
        color = Color(random.choice(colors))
        for i in bottom + middle + top + star:
            tree[i].color = color
            #input()
        for i in star + top[::-1] + middle[::-1] + bottom[::-1]:
            tree[i].color = Color('black')
        tree.color = Color('black')
        lala = not lala
except KeyboardInterrupt:
    tree.close()

