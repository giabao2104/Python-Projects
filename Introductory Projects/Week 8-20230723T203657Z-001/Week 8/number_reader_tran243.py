"""
Author: Gia Bao Tran, tran243@purdue.edu
Assignment: 08.5 - Number Reader
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
    with open ("random_numbers.txt","r") as fileout: #open file
        list1 = [] #initialise list
        terms = 0 #initialise term 
        for i in fileout:
            list1.append(int(i.strip()))
            terms +=1 #add one to every word.
        maximum = max(list1)
        minimum = min(list1) #calculation from list 
        summation = sum(list1)
        average = (summation / len(list1)) 
        print (f"{terms} numbers were read from the file.")
        print (f"Min: {minimum:,d}")
        print (f"Max: {maximum:,d}") #final print statements 
        print (f"Sum: {summation:,d}")
        print (f"Avg: {average:,.1f}")
    
if __name__ == '__main__':
    main()