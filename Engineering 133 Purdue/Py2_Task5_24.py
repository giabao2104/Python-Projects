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
from Py2_Task5_discriminant_24 import discriminant

def main():
    a = int(input("Input a: ")) #ask the user for inputs for a, b, c, and d to be used in the function
    b = int(input("Input b: "))
    c = int(input("Input c: "))
    d = int(input("Input d: "))
    disVal = discriminant(a, b, c, d) #use the function to evaluate the discriminant and assign it to a variable
    a = str(a) #Turned everything into strings to make te variables easier to print
    b = str(b)
    c = str(c)
    d = str(d)
    print("") #added a space between the input questions and the output for visual purposes
    print("The inputs are:") #Output everything
    print('a='+a+', b='+b+', c='+c+', d='+d)
    print('Real and distinct three roots:', disVal>0) #Compare the discriminant to 0 to analyze the function and display it to the user
    print('Real with at least two equal roots:', disVal==0)
    print('Conjugate pair of complex roots:', disVal<=0)

if __name__ == ("__main__"):
    main()

