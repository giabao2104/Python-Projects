"""
Author: Gia Bao Tran, tran243@purdue.edu
Assignment: 04.1 - Falling
Date: 09/27/2021

Description:
    This program will calculate the distance someone falls after a certain period of time due to gravity. 
Contributors:
    None

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
g = 8.87

def falling_dist(t):
    distance = (1/2*g*t**2)
    return distance
        
#function for the falling distance & return distance
def main():
    print ("Time (s)  Distance (m)")
    print ("----------------------")
    for t in range (5,51,5):
        if 0 <= t < 10:
            print (f"       {t}         {falling_dist(t):.1f}") 
        
        elif 10 <= t <= 15:
            print (f"      {t}         {falling_dist(t):.1f}") 
       
        elif 15 < t <= 45:
            print (f"      {t}        {falling_dist(t):.1f}") 

        elif 45 < t <= 50:
            print (f"      {t}       {falling_dist(t):.1f}")
#formatting with prints that are only called once & calling function 

if __name__ == "__main__":
    main()