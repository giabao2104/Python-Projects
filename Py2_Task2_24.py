"""
===============================================================================
ENGR 13300 Fall 2021

Program Description
   This program will give out the quality of ice-cream given its temperature and percentage of hydration. 

Assignment Information
    Assignment:     e.g. Team HW6 - PY 2 - Task 2 
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
    t = float(input("Enter the temperature of the ice cream[F]: "))
    h = float(input("Enter the hydration level of the ice cream[%]: "))

    if (t > 14) or (h > 60):
        print ("Danger")
#first set of conditions
        if t > 14:
            print ("High temperature")
    #a set of conditions within another set (nested if statements)   
        elif t <= 14:
            print ("High hydration")
        #elif for another condition
        elif t < 10:
            print ("Low temperature")
        else:
            print ("Low hydration")
        #everything else
    elif 10<=t<=14 and (55<=h<=60):
        print ("Normal")
    #elif statements for another set of condition

    else:
        print ("Warning")

        if t<10: 
            print ("Low temperature")
        else: 
            print ("Low hydration")

    #final else statement for warning

if __name__ == '__main__':
    main()