# Name: First Last
# Date:
# Period:
# Lab: turtle_polygon.py
# Description: Replace the '''missing code''' comments to make the program run as described
#
#     Style - Code format, whitespace and PEP-8 style is followed making code easy to read.
#     Comments - Blocks of code are well commented, every function has a descriptive comment.
#     Tests -   The program runs as described in the specifications without errors(passes all tests).
#       The square, pentagon, hexagon and octagon functions all work.
#       Three correct polygons are drawn.
#       Program runs without errors.

import turtle

# Create a new turtle pen Object
t = turtle.Pen()


def square(side_length):
    # TODO Use a for loop to draw a square with a given side length
    for x in range('''missing'''):
        t.forward('''missing''')
        t.left('''missing''')


def pentagon(side_length):
    # TODO Use a for loop to draw a pentagon with a given side length
    for x in range('''missing'''):
        t.forward('''missing''')
        t.left('''missing''')


def hexagon(side_length):
    # TODO Use a for loop to draw a hexagon with a given side length
    for x in range('''missing'''):
        t.forward('''missing''')
        t.left('''missing''')


def octagon(side_length):
    # TODO Use a for loop to draw a octagon with a given side length
    for x in range('''missing'''):
        t.forward('''missing''')
        t.left('''missing''')


def polygon(side_length, num_sides):
    # TODO Use a for loop to draw a polygon with a given side length and # of sides
    for x in range('''missing'''):   
        t.forward('''missing''')
        t.left('''missing''')


def main():
    t.penup()
    t.goto(-300, 300)
    t.pendown()

    square(50)  # draw a square with a side length of 50
    square(80)  # draw a square with a side length of 80
    t.penup()
    t.goto(-300, 100)
    t.pendown()

    pentagon(50)  # draw a pentagon with a side length of 50
    pentagon(80)    # draw a pentagon with a side length of 80
    t.penup()
    t.goto(-300, -100)
    t.pendown()

    hexagon(50)  # draw a hexagon with a side length of 50
    hexagon(80)     # draw a hexagon with a side length of 80
    t.penup()
    t.goto(-300, -300)
    t.pendown()

    octagon(50)  # draw an octagon with a side length of 50
    octagon(80)     # draw an octagon with a side length of 80
    t.penup()
    t.goto(0, 0)
    t.pendown()


    # TODO call the polygon function to make a square with a side length of 50
    '''missing'''

    # TODO call the polygon function to make a pentagon with a side length of 100
    '''missing'''

    # TODO call the polygon function to make a hexagon with a side length of 150
    '''missing'''

    # Keep the turtle window open
    turtle.mainloop()


# call the main() function
if __name__ == '__main__':
    main()
