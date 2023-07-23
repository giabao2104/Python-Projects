"""
Author: Gia Bao Tran, tran243@purdue.edu
Assignment: 01.1 - Vineyard
Date: 09/10/2021

Description:
    This program will help a farmer calculate the number of grapevines that he/she can fit into a row by inserting the length of rows, amount of space between vines and the ampount of space used by an end-post. 

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

    print("Enter each of the following quantities in meters.")

    x = (float(input("  How much space should be between the vines? ")))
    y = (float(input("  How wide is the end-post assembly? ")))
    z = (float(input("  How long is this row? ")))
    #input function. float so that answers will be more accurate

    no_of_vines = (str(int(((z-(2*y))/x))))
    #turning float to integer for because only full grapevines is possible

    print (f"\nThis row has enough space for {no_of_vines} vine(s).")

if __name__ == '__main__':
    main()



