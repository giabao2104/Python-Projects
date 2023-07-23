"""
Author: Gia Bao Tran, tran243@purdue.edu
Assignment: 01.3 - Cookie Recipe
Date: 09/10/2021

Description:
    This program will calculate the amount of ingredients (sugar, flour, butter) needed to bake the number of cookies inserted by the user. 

Contributors:
    None

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


def main():

    x = (int(input("How many cookies do you want to make? ")))
    #input function accepting floats 
    w = (round(x/48*1.75,2))
    y = (round(x/48,2))
    z = (round(x/48*2.5,2))
    #general formula for the three ingredients rounding to 2 decimal places 

    print (f"To make {x} cookies, you will need:")
    print (f"  {w:5.2f} cups of sugar")
    print (f"  {y:5.2f} cups of butter")  
    print (f"  {z:5.2f} cups of flour\n")
    #final printing statement


if __name__ == '__main__':
    main()