"""
Author: Gia Bao Tran, tran243@purdue.edu
Assignment: 02.5 - Fluid Mechanics
Date: 09/19/2021

Description:
    This program will calculate the viscosity of wter dependent on the user's inputs of velocity, temperature and diameter of a pipe 

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
def main():
    
    deg = (u"\N{DEGREE SIGN}")
    x = float(input(f"Enter the temperature in {deg}C as 5, 10, or 15: "))
    y = float(input("Enter the velocity of water in the pipe: "))
    z = float(input("Enter the pipe's diameter: "))

#set up input statements
    if x == 5:
        reynolds1 = format((y*z)/(1.49*10**-6),'.2e')
        print (f"At {x}{deg}C, the Reynolds number for flow at {y} m/s in a {z} m diameter pipe is {reynolds1}.")

    elif x == 10: 
        reynolds2 = format((y*z)/(1.31*10**-6),'.2e')
        print (f"At {x}{deg}C, the Reynolds number for flow at {y} m/s in a {z} m diameter pipe is {reynolds2}.")
    
    elif x == 15:
        reynolds3 = format((y*z)/(1.15*10**-6),'.2e')
        print (f"At {x}{deg}C, the Reynolds number for flow at {y} m/s in a {z} m diameter pipe is {reynolds3}.")

#if statements for 3 possible value of temperatures. 
if __name__ == "__main__":
    main()