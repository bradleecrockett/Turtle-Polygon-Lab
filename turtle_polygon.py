# Name: First Last
# Date:
# Period:
# Lab: turtle_polygon.py
# Description: Replace the '''missing code''' comments to make the program run as described
#
#     Style - Code format, whitespace and PEP-8 style is followed making code easy to read.
#     Comments - Blocks of code are well commented, every function has a descriptive comment.
#     Tests -   The program runs as described in the specifications without errors(passes all tests).
#       The square, pentagon, hexagon and octogon functions all work.
#       Three correct polygons are drawn.
#       Program runs without errors.

import turtle

# Create a new turtle pen Object
t = turtle.Pen()


def square(len):
    # TODO Use a for loop to draw a square with a given side length
    for x in range('''missing code'''):
        t.forward('''missing code''')
        t.left('''missing code''')


def pentagon(len):
    # TODO Use a for loop to draw a pentagon with a given side length
    for x in range('''missing code'''):
        t.forward('''missing code''')
        t.left('''missing code''')


def hexagon(len):
    # TODO Use a for loop to draw a hexagon with a given side length
    for x in range('''missing code'''):
        t.forward('''missing code''')
        t.left('''missing code''')


def octogon(len):
    # TODO Use a for loop to draw a octogon with a given side length
    for x in range('''missing code'''):
        t.forward('''missing code''')
        t.left('''missing code''')


def polygon(len, sides):
    # TODO Use a for loop to draw a polygon with a given side length and # of sides
    for x in range('''missing code'''):
        t.forward('''missing code''')
        t.left('''missing code''')


def main():
    t.penup()
    t.goto(100, 100)
    t.pendown()
    square(80)
    t.penup()
    t.goto(-100, 100)
    t.pendown()
    pentagon(80)
    t.penup()
    t.goto(-100, -100)
    t.pendown()
    hexagon(80)
    t.penup()
    t.goto(100, -100)
    t.pendown()
    octogon(80)
    t.penup()
    t.goto(0, 0)
    t.pendown()
    # call the polygon function to make a square with a side length of 50
    '''missing code'''
    # call the polygon function to make a pentagon with a side length of 100
    '''missing code'''
    # call the polygon function to make a hexagon with a side length of 150
    '''missing code'''
    # Keep the turtle window open
    turtle.mainloop()


# call the main() function
if __name__ == '__main__':
    main()
