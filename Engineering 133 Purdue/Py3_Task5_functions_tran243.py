"""
===============================================================================
ENGR 13300 Fall 2021

Program Description
    This program will output the MacLaurin's series for sin (x)^2 when the user input the limits of integration and max number of terms. 

Assignment Information
    Assignment:     e.g. Individual HW7 - PY 3
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
from Py3_Task2_function_24 import MyFactorial

def maclaurin_series(lower_limit,upper_limit,n):
    factorial_function = MyFactorial((2*n)+1)     
    maclaurin_formula = ((-1)**n)*(upper_limit**((4*n)+3))/(((4*n)+3)*factorial_function)
    maclaurin_formula2 = ((-1)**n)*(lower_limit**((4*n)+3))/(((4*n)+3)*factorial_function)
    return (maclaurin_formula-maclaurin_formula2)
#maclaurin series function calculated by importing the factorial function. 


