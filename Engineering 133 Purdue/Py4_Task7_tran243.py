"""
===============================================================================
ENGR 13300 Fall 2021

Program Description
    This program will find the occurances of a user-inputted word and how much that word constitute to the overall piece (in percentage). 

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

import string

def main():
    inputfilename = input("Enter the filename of the text file: ")
    word = (input("Enter the search word: ")).lower()
#user input of word and file
    inputfile = open(f'{inputfilename}','r')
    read = inputfile.read().lower().split() #read file
    repeated = 0 #starting number of occurence
    for i in read:
        x = i.strip(string.punctuation)
        if word == x:
            repeated += 1
    totalwords = (len(read)) #find total words
    percentage = ((repeated/totalwords)*100)
    print (f'The word "{word}" appears {repeated} out of {totalwords} words or {percentage:.2f}% of the time.') 
    inputfile.close() #close file     

if __name__ == "__main__":
        main()