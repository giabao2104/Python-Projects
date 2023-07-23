"""
===============================================================================
ENGR 13300 Fall 2021

Program Description
   This program will calculate the area of a parallelogram of side lengths 15 and 23 and the user will input an angle between 0 and 90. 

Assignment Information
    Assignment:     e.g. Team HW5 - PY 1 - Task 4 
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


def main():
    
    import math 
    #import math function
    x = int(input("Enter the angle of the parallelogram in degrees: "))
    xi = math.radians(x)
    #after input function, use math.radians to turn the input degrees into radians. 

    A = round(15*23*math.sin(xi),2) 
    #round answer to 2 decimal place.
    print (f"For given side lengths of 15[cm] and 23[cm], with an angle of {x}[degrees] between them, the area of a parallelogram is {A}[cm^2].")

if __name__ == '__main__':
    main()