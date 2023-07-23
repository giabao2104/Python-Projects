"""
===============================================================================
ENGR 13300 Fall 2021

Program Description
    This program willl calculate the distance a vehicle can travel powered by a wind turbine system.  

Assignment Information
    Assignment:     e.g. Team HW3 - PY 2
    Author:         Gia Bao Tran, tran243@purdue.edu
    Team ID:        LC1 - 24 

Contributor:    Alexi Argyros, aargyros@purdue.edu
                Tyler Serrato, tjserrat@purdue.edu
                Justin Shu, jgshu@purdue.edu
    My contributor(s) helped me:
    [  ] understand the assignment expectations without
        telling me how they will approach it.
    [  ] understand different ways to think about a solution
        without helping me plan my solution.
    [  ] think through the meaning of a specific error or
        bug present in my code without looking at my code.
    Note that if you helped somebody else with their code, you
    have to list that person as a contributor here as well.
    
ACADEMIC INTEGRITY STATEMENT
I have not used source code obtained from any other unauthorized
source, either modified or unmodified. Neither have I provided
access to my code to another. The project I am submitting
is my own original work.
===============================================================================
"""
def main():
# defines main function
    
 P = 700
# given value of power in watts

 p = 1.23
# given value of air density in kg/m^3

 v = 6
 # given value of wind velocity in m/s
 
 Cp = .4
# power coefficient (unitless)
 
 dv = distance_vehicle(s, t)
#shortens distance_vehhicle function

def distance_vehicle(s, t):
      #defines function
    
        dist = ((s/100000)*3600*(t))
        # formula to convert into distance
        
        return(dist)


def turbine_area(P, v, Cp, p):
        # defines function of turbine area
    
        A = (2*P)/(p*v*Cp)
#formula for fininng turbine area

        return(A)


s = int(input("Enter Speed: "))
        #required input values for speed

t = int(input("Enter Time: ")) 
#required input value for time

dv = distance_vehicle(s, t)
   

print(f'Distance: {dv} km')
# prints distance output

if __name__ == '__main__':
            main()
