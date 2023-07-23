"""
===============================================================================
ENGR 13300 Fall 2021

Program Description
    This program will seed 4 random numbers, rounded to 3 decimal places. These numbers and their sum can be represented in decimal and fraction forms. 

Assignment Information
    Assignment:     e.g. Individual HW6 - PY 1
    Author:         Gia Bao Tran, tran243@purdue.edu
    Team ID:        LC1 - 24 

Contributor: None
    My contributor(s) helped me:
    [  ] understand the assignment expectations without
        telling me how they will approach it.
    [  ] understand different ways to think about a solution
        without helping me plan my solution.
    [  ] think through the meaning of a specific error or
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
    import random 

    random.seed(int(input("Enter the seed: ")))

    w =  (str(round(random.uniform(0,100),3)))
    wi = float(w)
#set up variables. random.uniform generate a random float. use round function for 3 decimal places and string to use f-strings later. 
    x =  (str(round(random.uniform(0,100),3)))
    xi = float(x)
    y =  (str(round(random.uniform(0,100),3)))
    yi = float(y)
    z =  (str(round(random.uniform(0,100),3)))
    zi = (float(z))

    total = (sum((wi,xi,yi,zi)))
    total_round = (round(total,3))
    #sum function to find sum of 4 numbers. Round to 3 decimal places. 

    from fractions import Fraction
    fw = (str(Fraction(wi).limit_denominator(100)))
    fx = (str(Fraction(xi).limit_denominator(100)))
    fy = (str(Fraction(yi).limit_denominator(100)))
    fz = (str(Fraction(zi).limit_denominator(100)))
    ft = (str(Fraction(total_round).limit_denominator(100)))
    #Set up variables to form fractions and limit denominator so that it is below 100 as asked. 

    print("First random number : " + w)
    print("Second random number : " + x)
    print("Third random number : " + y)
    print("Fourth random number : " + z)
    print(f"Sum from decimals: {w} + {x} + {y} + {z} = {total_round}")
    print(f"Sum from fractions: {fw} + {fx} + {fy} + {fz} = {ft}")
    #print statements using variables and f-strings. 
if __name__ == '__main__':
    main()