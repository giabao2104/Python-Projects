"""
Author: Gia Bao Tran, tran243@purdue.edu
Assignment: 02.1 - Leap Year
Date: 09/19/2021

Description:
    This program will ask the user to input a year and determine whether it is a leap year or not. 

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

    x = int(input("Please input a year: "))
    leap = "29"
    non_leap = "28"
#asked for user input and set up variables for leap & non-leap years 

    if x % 100 == 0 and x % 400 == 0:
        print (f"In the year {x}, February has {leap} days.")

    elif x % 100 != 0 and x % 4 == 0:
         print (f"In the year {x}, February has {leap} days.")
    
    else:
        print ((f"In the year {x}, February has {non_leap} days."))



if __name__ == '__main__':
    main()