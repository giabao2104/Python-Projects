"""
Author: Gia Bao Tran, tran243@purdue.edu
Assignment: 08.3 - File Stats
Date: 11/06/2021

Description:
    This program will calculate the multiple of n (any integer given) of a set of numbers in a list

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
def main():
    with open('frontiero_v_richardson.txt') as filein: #open the file 
        numberlines = 0 #initialise variables
        numberwords = 0
        for line in filein: #go through the for loop 
            line1 = line.strip("\n") #strip the spaces
            words = line1.split()
            numberlines += 1
            numberwords += len(words) 
        avg = numberwords/numberlines

    print (f"Total number of words: {numberwords}")
    print (f"Total number of lines: {numberlines}")  #print statements
    print (f"Average number of words per line: {avg:.1f}")

if __name__ == '__main__':
    main()