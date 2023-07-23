"""
Author: Gia Bao Tran, tran243@purdue.edu
Assignment: 07.1 - Multiples of N
Date: 10/25/2021

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

def multiples_of (int,list_of_numbers):
    list1 = []
    for i in range(0,len(list_of_numbers)):
        if list_of_numbers[i] % int != 0: 
            continue
        else:
            list1.append(list_of_numbers[i]) #if it is divisible by the integer then add it to the list
    return list1

def main():
    int = 13 
    list_of_numbers = [19,1599,-546,10,39,-58,1,85,201,-91,286,799,406]
    list1 = multiples_of(int,list_of_numbers) #call the function 
    print ("Original list of numbers:") 
    print(f"  {list_of_numbers}")
    print(f"Numbers in the list that are multiples of {int}:")
    print (f"  {list1}")
#final print statements
if __name__ == '__main__':
    main()