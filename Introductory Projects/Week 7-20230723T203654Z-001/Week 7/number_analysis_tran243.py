"""
Author: Gia Bao Tran, tran243@purdue.edu
Assignment: 07.2 - Number Analysis
Date: 10/25/2021

Description:
    This program will get a number in a list and analyse its max, min and average 

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

def get_number_list():

    list_of_numbers = []
    for int in range(1,11,1):
        if int <=10:
            user_input = float(input(f"  number {int:2d} of 10: "))
            list_of_numbers.append(user_input) #append to the list

    return list_of_numbers

def main():
    
    print ("Enter 10 numbers:")
    list_of_numbers = get_number_list()
    maximum = max(list_of_numbers) #find the maximum
    minimum = min(list_of_numbers)#find the minimum
    summation = sum(list_of_numbers) #find the sum
    sumbylen = summation/len(list_of_numbers) #find the average
    print(f"Highest number: {maximum:.2f}")
    print(f"Lowest number: {minimum:.2f}")
    print(f"Total: {summation:.2f}")
    print (f'Average: {sumbylen:.2f}') #print statements

if __name__ == '__main__':
    main()