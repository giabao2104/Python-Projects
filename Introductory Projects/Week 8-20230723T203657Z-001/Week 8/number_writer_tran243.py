"""
Author: Gia Bao Tran, tran243@purdue.edu
Assignment: 08.4 - Number Writer
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
import random
def main():
    userinp = int(input("How many numbers would you like? ")) #input
    with open ("random_numbers.txt","w+") as fileout: #open
        for i in range (userinp):
            x = str(random.randint(1019,1215)) #generate random number
            fileout.write(f"{x}\n") #write in the file
    fileout.close() #close
if __name__ == '__main__':
    main()