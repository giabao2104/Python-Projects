"""
===============================================================================
ENGR 133 Fall 2021
Program Description
    Quiz 6 - This program reads a text file and asks the student to complete the 
    program to write the output to a text file. 

Assignment Information
    Assignment:     Py4 Quiz 6
    Author: Gia Bao Tran       


ACADEMIC INTEGRITY STATEMENT
I have not used source code obtained from any other unauthorized
source, either modified or unmodified. Neither have I provided
access to my code to another. The project I am submitting
is my own original work.
===============================================================================
"""

def main():
    # Open the file as the name ipfile
    with open('Quiz6_input.txt','r') as ipfile:
        score = []
        lines = ipfile.readlines()
        #separate the scores into a list
        for i in lines:
            line = i.split()
            score.append(float(line[1]))

    # add your solution below
    ipfile.write ("The Low Score is " + (score[2]) + ".")
    ipfile.close()

    ipfile = open('Quiz6_input.txt','r')
    print(ipfile.read())

    x = int(min(score))
    print (f"The Low score is: {x}")
            
if __name__ == '__main__':
    main()