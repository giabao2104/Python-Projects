"""
===============================================================================
ENGR 13300 Fall 2021

Program Description
    This program will calculate the sum of the fibonacci sequence up to number of the user input. 

Assignment Information
    Assignment:     e.g. Team HW7 - PY 3
    Author:         Gia Bao Tran, tran243@purdue.edu
    Team ID:        LC1 - 24 

Contributor:    Alexi Argyros, aargyros@purdue.edu
                Tyler Serrato, tjserrat@purdue.edu
                Justin Shu, jgshu@purdue.edu
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
    i = 0
    x = [0,1]
    j = int(input('How many numbers long is the fibonacci sequence? '))
    if (j == 1):
        x = [0]
        
    elif (j == 2):
        pass
    else:
        while (i < j - 2):
            x.append(x[-1] + x[-2])
            i += 1
    print (x)

if __name__ == '__main__':
    main()
