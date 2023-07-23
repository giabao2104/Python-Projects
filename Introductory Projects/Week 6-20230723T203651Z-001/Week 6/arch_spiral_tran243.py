"""
Author: Gia Bao Tran, tran243@purdue.edu
Assignment: 06.4 - Arch Spiral
Date: 10/17/2021

Description:
    This program will draw an Archimedian Spiral using math and turtle modules

Contributors:
    Name, login@purdue.edu [repeat for each]

My contributor(s) helped me:
    [ ] understand the assignment expectations without
        telling me how they will approach it.
    [ ] understand different ways to think about a solution
        without helping me plan my solution.
    [ ] think through the meaning of a specific error or
        bug present in my code without looking at my code.
    Note that if you helped somebody else with their code, you
    have to list that person as a contributor.

Academic Integrity Statement:
    I have not used source code obtained from any unauthorized
    source, either modified or unmodified; nor have I provided
    another student access to my code.  The project I am
    submitting is my own original work.
"""

from turtle import *
from math import radians,pi,cos,sin
# Import additional modules below this line.


# Write new functions below this line (starting with unit 4).


def start():
    """This function initializes the window and the turtle.
    Do not modify this function.
    """
    setup(564, 564)
    width('5')


def main():
    """Write your mainline logic here."""


    for angle in range (0,2161,1): #iterate 6 times 
        x_coor = (angle/(pi**2))*cos(radians(angle)) #angle for x 
        y_coor = (angle/(pi**2))*sin(radians(angle)) 
        goto(x_coor,y_coor) 


if __name__ == '__main__':
    # Do not change this part
    start()
    main()
    done()
