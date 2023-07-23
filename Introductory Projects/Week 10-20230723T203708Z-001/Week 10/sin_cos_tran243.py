"""
Author: Gia Bao Tran, tran243@purdue.edu
Assignment: 10.4 - Sin Cos
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
import numpy as np 
import math

def main():
    a = np.arange(0,2*np.pi,0.1) #sets a range for the 'a' value
    ysin = np.sin(a) #create functions for sin and cos
    ycos = np.cos(a)
    
    xlabels = ["$\\pi/2$", "$\\pi$", "$3\\pi/2$", "$2\\pi$"]
    ylabels = ["−1", "1"]
    fig, ax = plt.subplots()
    
    plt.plot(a,ysin,"r")
    plt.plot(a,ycos,"b")
    
    for i in ["top", "right"]: #by using the foor loops, we can make sure the spines and axis are in the correct position.
        ax.spines[i].set_visible(False)
    for j in ["bottom","left"]:
        ax.spines[j].set_position("zero")
    ax.set_ylim(-1,1)
    ax.set_xlim(0,2*math.pi)
    ax.set_yticks([-1,1])
    ax.set_xticks([math.pi/2,math.pi,3*math.pi/2,2*math.pi])
    ax.set_yticklabels(ylabels)
    ax.set_xticklabels(xlabels)
    plt.title("Graph of Sin and Cos") #

    plt.show()
if __name__ == '__main__':
    main()