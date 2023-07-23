"""
===============================================================================
ENGR 13300 Fall 2021

Program Description
    This program will output the MacLaurin's series for sin (x^2) when the user input the limits of integration and max number of terms. 

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
n = 0 
from Py3_Task2_function_24 import MyFactorial

factorial_function = MyFactorial((2*n)+1)

from Py3_Task5_functions_tran243 import maclaurin_series



def main():
    try:
        lower_limit = float(input("Enter the lower limit of integration: "))
        print("")
    except ValueError:
        print ("Error 1: Input integer or floating-point number")
        return

    try:
        upper_limit = float(input("Enter the upper limit of integration: "))
        print("")
    except ValueError:
        print ("Error 1: Input integer or floating-point number")
        return
    
    try:
        decimal_places = float(input("Enter the number of decimal places for convergence: "))
        print("")
        if decimal_places < 0:
            print ("Error 2: Input a positive integer.")
    except ValueError:
        print ("Error 1: Input integer or floating-point number")
        return


    try:
        max_terms = int(input("Enter the maximum number of terms: "))
        print("")
        if max_terms < 0:
            print ("Error 2: Input a positive integer.")
    except ValueError:
        print ("Error 1: Input integer or floating-point number")
        return


#present all error cases with user inputs 

    sum_of_series = 0
    list_of_series = []
#start with sum of series = 0
    print("Approximations:")
    for n in range (0,max_terms):
        maclaurin = maclaurin_series(lower_limit,upper_limit,n)
#activate the maclaurin series function
        sum_of_series += maclaurin
#add the the value to the previous term and take on that term
        list_of_series.append(round(sum_of_series,3))
        print(f"n = {n}: sum = {sum_of_series:.3f}")
        if n >= 3:
            if list_of_series [n] == list_of_series [n-1] == list_of_series [n-2]:
                print (f"The integral from {lower_limit:.1f} to {upper_limit:.1f} is estimated to be {sum_of_series:.3f}.")
                print (f"Total number of terms: {max_terms}") 
                return
 #for loop to calculate the sum of series using the imported maclaurin function to calculate the sum of series.


#final print statements

