"""
Ask user for color.
"""
from tree import RGBXmasTree
from colorzero import Color

tree = RGBXmasTree()

try:
    while True:
        color = input()
        tree.color = Color(color)
except KeyboardInterrupt:
    tree.off()
    tree.close()
