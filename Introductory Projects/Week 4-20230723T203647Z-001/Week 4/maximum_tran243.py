"""
Author: Gia Bao Tran, tran243@purdue.edu
Assignment: 04.2 - Maximum
Date: 10/02/2021

Description:
    This program take user input for 2 values and return the value that is greater out of the two. 
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
def max_of_two (x,y):
    if x > y:
        return x
    else:
        return y 
#set up the function to find the max of two variables 
def main():
    x = int(input("Enter the first integer: "))
    y = int(input("Enter the second integer: "))
#ask for user input
    print (f"The number {max_of_two(x,y)} is greater.")
#print the maximum number

if __name__ == "__main__":
    main()