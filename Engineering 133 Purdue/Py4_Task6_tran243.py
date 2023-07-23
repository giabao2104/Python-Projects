"""
===============================================================================
ENGR 13300 Fall 2021

Program Description
    This program will ask the user to input a file name and output file name. The program will make adjustments and add to steps number before each instruction.

Assignment Information
    Assignment:     e.g. Individual HW8 - PY 4
    Author:         Gia Bao Tran, tran243@purdue.edu
    Team ID:        LC1 - 24 

Contributor: None
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
    
    inputfile = (input("Enter the filename of the input file: "))
    outputfile = (input("Enter the filename of the output file: "))
#user input of input and output files
    with open (f'{inputfile}','r') as filein: 
        with open (f'{outputfile}','r+') as fileout: #open the files
            x = 1 #set x to 1 as the beginning (step 1)
            for line in filein:
                phrase = (f"Step {x}: " + line) #turn it into 1 argument to fit the fileout.write() function
                fileout.write(phrase)
                x+=1 #x increases by 1 each time
                print (fileout.read()) #read 

if __name__ == "__main__":
    main()