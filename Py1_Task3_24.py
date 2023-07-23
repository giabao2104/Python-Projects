"""
===============================================================================
ENGR 13300 Fall 2021

Program Description
   This program will calculate the surface area of a cone given the radius and height.

Assignment Information
    Assignment:     e.g. Team HW5 - PY 1 - Task 3
    Author:         Gia Bao Tran, tran243@purdue.edu
    Team ID:        LC1 - 24 

Contributor:    Alexi Argyros, aargyros@purdue.edu
                Tyler Serrato, tjserrat@purdue.edu
                Justin Shu, jgshu@purdue.edu [repeat for each]
    My contributor(s) helped me:
    [ x ] understand the assignment expectations without
        telling me how they will approach it.
    [ x ] understand different ways to think about a solution
        without helping me plan my solution.
    [ x ] think through the meaning of a specific error or
        bug present in my code without looking at my code.
    Note that if you helped somebody else with their code, you
    have to list that person as a contributor here as well.
    
ACADEMIC INTEGRITY STATEMENT
I have not used source code obtained from any other unauthorized
source, either modified or unmodified. Neither have I provided
access to my code to another. The project I am submitting
is my own original work.
===============================================================================
"""
r = input("enter value for the radius: ")
#set input function for the radius

ri = float(r)
#make sure ri is a float, float is more flexible than integer in case the inserted number is not an integer


h = input("enter value for the height: ")
#set input function for the height

hi = float(h)
#make sure hi is a float, float is more flexible than integer in case the inserted number is not an integer


from math import pi,sqrt
#import the pi & square root function from math because its the only 2 we need

l = (sqrt((hi**2)+(ri**2)))
#calculate slant of cone as it is apart of the formula to find SA of cone

A = (pi*ri**2+pi*ri*l)

def main():

    print (str(A)+'cm^2')

if __name__ == '__main__':
    main()


