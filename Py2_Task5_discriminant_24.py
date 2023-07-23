"""
===============================================================================
ENGR 13300 Fall 2021

Program Description
   This program takes a cubic function and calculate the discriminant. Discriminant reveals the number and realness of roots.  

Assignment Information
    Assignment:     e.g. Team HW6 - PY 2 - Task 5 
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
def discriminant(a, b, c, d): #Establish the function
    dis = (b**2)*(c**2)-4*a*(c**3)-4*(b**3)*d-27*(a**2)*(d**2)+18*a*b*c*d
    #This is the formula, assigned to a variable in the function
    return dis
    #return the answer
