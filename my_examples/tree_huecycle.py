"""
Cycle true hue, from the original repo.
"""
from tree import RGBXmasTree
from colorzero import Color, Hue

tree = RGBXmasTree()

tree.color = Color('red')

try:
    tree.brightness = 0.1
    while True:
        tree.color += Hue(deg=5)
except KeyboardInterrupt:
    tree.close()
