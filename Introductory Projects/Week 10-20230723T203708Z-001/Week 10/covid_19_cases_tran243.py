"""
Author: Gia Bao Tran, tran243@purdue.edu
Assignment: 10.3 - Covid 19 Cases
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
import datetime

def main():
        filein = open ('indiana_covid_19_data_fall_2021.txt')#open file as filein
        data = filein.readlines() # read the lines
        filein.close()
        
        dates = []
        newcases = []
        xaxis = []
        yaxis = []
        z = 0
        
        for i in range(len(data)): #first for loop to sort through data
            x = data[i]
            y = x.split(' ')
            date1 = y[0]
            positive = y[2]
            dates.append(date1)
            newcases.append(positive)
        
        for j in range(len(newcases)): #second for loop to manipulate data
            x = float(int(newcases[j])/1000)
            z = x + z
            yaxis.append(z)
        
        print(yaxis)
        
        for k in dates: #this for loop is done to create the year, month and day
            year,month,day = k.split('-')
            daytime = datetime.date(int(year), int(month), int(day))
            xaxis.append(daytime)
            xaxis.append(daytime)
        
        fig,ax = plt.subplots() #final plots follwoing the different requirements
        ax.bar(xaxis,yaxis,width = 1)
        plt.xlabel("Date")
        plt.ylabel("Number of Cases (in thousands)")
        ax.set_yticks([0,200,400,600,800,1000,1200])
        ax.set_ylim(0,100)
        ylabel = ['0','200','400','600','800','1000','1200']
        ax.set_yticklabels(ylabel)
        fig.autofmt_xdate()
        plt.title("Positive COVID-19 Cases in Indiana")
        plt.show() # show the graph on the plot

if __name__ == '__main__':
    main()