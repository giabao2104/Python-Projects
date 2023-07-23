"""
===============================================================================
ENGR 13300 Fall 2021

Program Description
    Calculating the pressure and temperature of a gas and figuring out an optimal state through Van Der Waal's equation of state.

Assignment Information
    Assignment:     e.g. Individual HW7 - PY 2
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

import Py2_Task7_functions_tran243 as funct
#import the function file 
def main():
    p = funct.solve_pressure()
    t = funct.first_temp()
    td = funct.dec_temp()
#set up the function in the local main function
    def first_example():
        print (f"Initial resulting pressure = {p}")
        print()
        print (f"Required temperature increment for in-range pressure = {t} [K]")
        print ("New pressure = 30 [atm]")
    #apply the variables using f-strings and add additional info for each example
    def second_example():
        print(f"Resulting pressure = {p} [atm]")
        print()
        print ("The pressure is within the acceptable range")
    #example 2
    def third_example():
        print (f"Initial resulting pressure = {p} [atm]")
        print()
        print (f"Required temperature increment for in-range pressure = {(td-t)} [K]")
        print ("New pressure = 35 [atm]")
    #example 3
    def fourth_example():
        print(f"Pressure is {p} [atm]")
        print()
        print ("Error:999 - pressure at unacceptable level. Danger imminent! Sound the alarm and run away to safety.")
    #example 4
    if (p<30):
        first_example()
    elif (p>=30) and (p<=35):
        second_example()
    elif (p<=100) and (p>35):
        third_example()
    else:
        fourth_example()
#conditional statements to know when to use which function. 

if __name__ == "__main__":
    main()
