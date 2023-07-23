"""
Author: Gia Bao Tran, tran243@purdue.edu
Assignment: 06.1 - Math Quiz
Date: 10/13/2021

Description:
    This program will use modules to give the user a math problem they need to solve

Contributors:
    Name, login@purdue.edu [repeat for each]

My contributor(s) helped me:
    [ ] understand the assignment expectations without
        telling me how they will approach it.
    [ ] understand different ways to think about a solution
        without helping me plan my solution.
    [ ] think through the meaning of a specific error or
        bug present in my code without looking at my code.
    Note that if you helped somebody else with their code, you
    have to list that person as a contributor.

Academic Integrity Statement:
    I have not used source code obtained from any unauthorized
    source, either modified or unmodified; nor have I provided
    another student access to my code.  The project I am
    submitting is my own original work.
"""

import random

def random_number(x):
    if x == 2:
        a = 10
        b = 99
    elif x == 3:
        a = 100
        b = 999
    number1 = random.randint(a,b)
    return number1 
#user defined function - argument determine the number of digits 

def main():
    num1 = random_number(2)
    num2 = random_number(3)
    print (f"   {num1}")
    print (f"+ {num2}")
    print ("-----")
    print ("= ",end='')

    userinput = int(input(""))
    sum = num1 + num2
    if userinput == sum: #if statements to determine whether the answers are correct. 
        print ("Correct -- Good Work!")
    else: 
        print (f"Incorrect. The correct answer is {sum}.") #if its wrong, give the write answer

    

if __name__ == '__main__':
    main()