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
R = 0.0820573661
a = 3.59 
b = 0.0427
x = round(float(input("Input Initial Temperature in Kelvin: ")),1)
print()
y = float(input("Input molar volume in L/mol: "))
y2 = (y**2)
#set up all variables 
def solve_pressure():

    print("Initial conditions:")
    print()
    print (f'Molar volume = {y} [L/mol]')
    print (f"Initial temperature = {x} [K]")
    p = round((R*x)/(y-b)-(a/y2),4)
    return p
#function to calculate the pressure 

def inc_temp():
    temp = (((y-b)*(30+((a)/(y2)))/(R)))
    return temp
#function for increment temperature 
def dec_temp():
    temp = (((y-b)*(35+((a)/(y2)))/(R)))
    return temp
#function for decrement temperature
def first_temp():
    return x
#initial temperature
