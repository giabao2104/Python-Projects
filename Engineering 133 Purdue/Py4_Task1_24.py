"""
===============================================================================
ENGR 13300 Fall 2021

Program Description
    This program will output the name, total age in years and total age in seconds into a text file. 

Assignment Information
    Assignment:     e.g. Team HW8 - PY 4
    Author:         Gia Bao Tran, tran243@purdue.edu
    Team ID:        LC1 - 24 

Contributor:    Alexi Argyros, aargyros@purdue.edu
                Tyler Serrato, tjserrat@purdue.edu
                Justin Shu, jgshu@purdue.edu [repeat for each]
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
    last_name = input("Enter your last name: \n")
    print()
    first_name = input("Enter your first name: \n")
    print()
    age = int(input("Enter your age in whole years: \n"))
    print()
    last_bday = int(input("Enter the days elapsed since your last birthday: \n"))
    n = float((last_bday)/365.242199)
    total_age = (age+n)
    age_seconds = int(31536000*total_age)
#set up variables user input and calculations of age in seconds and years. 

    text_file = open('Py4_Task1_output_24.txt','w')
    text_file.write(f"{first_name} {last_name} \nYou are {total_age} years old. \nYou are {age_seconds} seconds old.")
    text_file.close()
#open file, and print using (.write) the required lines with f-strings and close the file

    text_file = open('Py4_Task1_output_24.txt','r')
    print(text_file.read())
#open the file to read only and print it. 

if __name__ == "__main__":
    main()