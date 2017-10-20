# Name: First Last
# Date:
# Period:
# Lab: turtle_polygon.py
# Description: Replace the '''missing code''' comments to make the program run as described
#
#     Style - Code format, whitespace and PEP-8 style is followed making code easy to read.
#     Comments - Blocks of code are well commented, every function has a descriptive comment.
#     Tests -   The program runs as described in the specifications without errors(passes all tests).
#       Three correct polygons are drawn.
#       Program runs without errors.

import turtle

# Create a new turtle pen Object
t = turtle.Pen()

def polygon(len: float, sides: int):
    """Use a for loop to draw a polygon with a given side length and # of sides"""
    for x in range('''missing code'''):
        t.forward('''missing code''')
        t.left('''missing code''')

def main():
    # call the polygon function to make a square with a side length of 50
    '''missing code'''
    # call the polygon function to make a pentagon with a side length of 100
    '''missing code'''
    # call the polygon function to make a hexagon with a side length of 150
    '''missing code'''

# call the main() function
main()

# Keep the window open at the end of the program
turtle.mainloop()
