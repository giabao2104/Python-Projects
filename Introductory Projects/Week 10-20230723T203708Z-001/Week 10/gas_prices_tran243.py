"""
Author: Gia Bao Tran, tran243@purdue.edu
Assignment: 10.2 - Gas Prices
Date: 11/06/2021

Description:
    This program will collect info from user and plot monthly sales in a pie chart. 
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
import matplotlib.pyplot as plt

def main():
    with open ("2008_Weekly_Gas_Averages.txt") as filein: #open the text file as file in
        prices = filein.readlines() #read the lines
        
        newprices = []
        weeks = [] # create the initial lists
    
        for x in range (0,len(prices)): # for loop to run through each value
            price = prices[x]
            price = float(price.strip('\n')) #return as a float and strip the new line
            newprices.append(price)
            weeks.append(x+1)
        
        fig,ax = plt.subplots()
        plt.plot(weeks,newprices)
        ax.set_xlim(1.0,52.0) #final printing statements as required.
        ax.set_ylim(1.5,4.25)
        plt.title("2008 Weekly Gas Prices")
        plt.xlabel("Weeks (by number)")
        plt.ylabel("Average Price (dollars/gallon)")
        ax.grid()
        
if __name__ == '__main__':
    main()