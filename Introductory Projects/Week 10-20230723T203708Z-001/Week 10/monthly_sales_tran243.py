"""
Author: Gia Bao Tran, tran243@purdue.edu
Assignment: 10.1 - Monthly Sales
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
import matplotlib.pyplot as plt #import matplot

def main():
    list_of_months = ['January','February','March','April',"May",'June','July','August','September','October','November','December']
    values = [] #add the values to a list
    for i in list_of_months: #goes through each month
        Userinp = int(input(f"Enter the sales for {i}: ")) #print the months
        values.append(Userinp) #append that value into another list.
    
    c = ('#4D4038','#BAA892','#5B6870','#6E99B4','#A3D6D7','#085C11','#849E2A','#C3BE0B','#E9E45B','#6B4536','#B46012','#FF9B1A') #all colours
    fig, ax = plt.subplots()#create subplots.
    ax.pie(values, colors=c, labels=list_of_months)#plot a pie graph
    plt.title("Monthly Sales Values") #title of the plot
    plt.show()#show plot
if __name__ == '__main__':
    main()
