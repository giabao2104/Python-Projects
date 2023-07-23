"""
Author: Gia Bao Tran, tran243@purdue.edu
Assignment: 07.3 - Roll Analysis
Date: 10/25/2021

Description:
    This program will simulate two 6-faced dice and calculate the frequency of obtaining a specific answer 

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
def roll_d6():
    list6 = [1,2,3,4,5,6]
    roll6 = random.choice(list6) #choose a number from the dice
    return roll6 

def get_2d6_rolls(x):
    i = 1
    empty = []
    while i <= x: #execute however many time
        list12 = roll_d6() + roll_d6() #add them together
        empty.append(list12)
        i+=1
    return (empty) #return list
        
def main():
    x = 1000000
    mainlist = get_2d6_rolls(x) 
    r = [0,0,0,0,0,0,0,0,0,0,0] #initial list
    for i in mainlist:
        r[i-2]+=1 #for loop to add to list
    print ("Roll  Frequency")
    z = 2
    for j in range (0,11):
        r[j] = (r[j]/x)*100
        print (f" {z:2d}    {r[j]:5.2f}%") # work in the for loop
        z+=1
    



if __name__ == '__main__':
    main()