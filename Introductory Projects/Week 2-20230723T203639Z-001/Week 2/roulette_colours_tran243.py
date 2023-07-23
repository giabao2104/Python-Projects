"""
Author: Gia Bao Tran, tran243@purdue.edu
Assignment: 02.3 - Roulette Colours
Date: 09/19/2021

Description:
    This program give the colour on the roulette wheel depending on the number the user chooses.  

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
    x = int(input("Please choose a pocket number: "))
#insert function
    if x == 0:
        print (f"  Pocket number {x} is green.")
#setting up different conditon    
    elif 1 <= x <= 10 or 19 <= x <= 28: 
        if x % 2 == 0:
            print (f"  Pocket number {x} is black.")
        else: 
            print (f"  Pocket number {x} is red.")
#within an elif there are different permutations    
    elif 11 <= x <= 18 or 29 <= x <= 36: 
        if x % 2 == 0:
            print (f"  Pocket number {x} is red")
        else: 
            print (f"  Pocket number {x} is black.")
    
    else: 
        print ("  Invalid input!")
#everything out of range is invalid
if __name__ == '__main__':
    main()