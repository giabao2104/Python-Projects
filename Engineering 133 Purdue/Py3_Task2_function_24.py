"""
===============================================================================
ENGR 13300 Fall 2021

Program Description
    Take user input to calculate factorials

Assignment Information
    Assignment:     Team HW7 - PY3 
    Author:         Name, aargyros@purdue.edu
    Team ID:        LC1 - 24

Contributor:   Gia Bao Tran, tran243@purdue.edu
               Tyler Serrato, tjserrat@purdue.edu
               Justin Shu, jgshu@purdue.edu
    My contributor(s) helped me:
    [ ] understand the assignment expectations without
        telling me how they will approach it.
    [ ] understand different ways to think about a solution
        without helping me plan my solution.
    [ ] think through the meaning of a specific error or
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
def MyFactorial(n):
   factorial = 1
   if n > 0: #The factorial function will only run if the number is greater than or equal to 1
       for i in range (1,n+1):
           factorial = factorial*i
       return factorial
#factorial function
   elif n == 0:
       print ("Factorial of 0 is 1.")
 
   else: #Otherwise the factorial cannot be produced, so an error is returned.
       print ("Error[Negative input].") 







