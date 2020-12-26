"""
Ask user for color as cmd argument
"""
from tree import RGBXmasTree
from sys import argv
from colorzero import Color

tree = RGBXmasTree()

tree.color = Color(argv[1])

tree.close()
