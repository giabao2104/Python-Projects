"""
===============================================================================
ENGR 13300 Fall 2021

Program Description
    This program will calculate capacitance for 2 capacitors set in both series and parallel circuits. 

Assignment Information
    Assignment:     e.g. Individual HW7 - PY 1
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
    from math import sqrt,e
#importing sqrt and e to simplify the math input later

    first_capacitor = round(float(input("Input the first capacitor value [\u00b5F]: ")),1)
    second_capacitor = (float((sqrt(2.72)*e)))
    second_capacitor1 = round(second_capacitor,1)
    capacitor_list = [first_capacitor,second_capacitor]
    inverse_cap1 = (1/first_capacitor)
    inverse_cap2 = (1/second_capacitor)
    list_inverse = [inverse_cap1,inverse_cap2]
#setting up variables and lists to input and calculate each capacitor

    parallel_capacitance = (round(sum(capacitor_list),1))
    series_capacitance = (sum(list_inverse))
    series_capacitance1 = (round(1/series_capacitance,1))
#sum of capacitance, turned into strings to become f-strings

    type = ("Type")
    parallel = ("Parallel")
    series = ("Series")
    first = ("First")
    second = ("Second")
    equivalent_capacitance = ("Equivalent Capacitance")

    print (f"{type}              {first}         {second}         {equivalent_capacitance}")
    print (f"{parallel}   {first_capacitor:11.1f} \u00b5F {second_capacitor1:10.1f} \u00b5F {parallel_capacitance:12.1f} \u00b5F")
    print (f"{series}     {first_capacitor:11.1f} \u00b5F {second_capacitor1:10.1f} \u00b5F {series_capacitance1:12.1f} \u00b5F")
#3 line printing output. 

if __name__ == '__main__':
    main()