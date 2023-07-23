"""
Author: Gia Bao Tran, tran243@purdue.edu
Assignment: 08.2 - Phone Number Converter
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
def convert_number(userinp):
    number = userinp.upper()
    realnumber = ("") #initialising the variables needed in the function 
    for i in number: #go through each number
        for j in range (len(i)): # length of each number
            if i[j] in "WXYZ":
                realnumber = realnumber + "9"
            elif i[j] in "TUV":
                realnumber = realnumber + "8"
            elif i[j] in "PQRS":
                realnumber = realnumber + "7"
            elif i[j] in "MNO":
                realnumber = realnumber + "6"
            elif i[j] in "JKL":
                realnumber = realnumber + "5"
            elif i[j] in "GHI":
                realnumber = realnumber + "4"
            elif i[j] in "DEF":
                realnumber = realnumber + "3"
            elif i[j] in "ABC":
                realnumber = realnumber + "2"
            else:
                realnumber = realnumber + i[j]

    y = realnumber
    #print (y)
    return y


def main():
    userinp = (input("Enter a telephone number: ")) #make everything upper-case
    print (f"The phone number is {convert_number(userinp)}") #print statement

if __name__ == '__main__':
    main()