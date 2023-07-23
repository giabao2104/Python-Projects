"""
===============================================================================
ENGR 13300 Fall 2021

Program Description
    Calculate output of a light going through a different medium. The outgoing ray could be refracting at a certain angle or experiencing total internal reflection when the incoming angle is larger than the total internal reflection.

Assignment Information
    Assignment:     e.g. Individual HW6 - PY 2
    Author:         Gia Bao Tran, tran243@purdue.edu
    Team ID:        LC1 - 24 

Contributor: None
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
from math import sin, asin, tan, radians, degrees

def calc_crit_angle(n1,n2):
    if n1>n2:
        critical_angle = (asin((n2*(sin(radians(90))))/n1))
        return degrees(critical_angle)
    else:
        return 0
#crit angle function
    
def calc_exit_angle (n1,n2,theta_in):
    outgoing_angle = asin((n1*(sin(radians(theta_in))))/n2)
    return degrees(outgoing_angle)
#exit angle function

def calc_dist(d1, theta_1,d2,theta_2):
    d3 = (d1*(tan(radians(theta_1)))) + (d2*(tan(radians(theta_2))))
    return d3
#distance calculation function

def main():
    n2 = 1.44
    d1 = 3.8
    d2 = 9.1 

    theta_in = (float(input("Enter the incoming angle in degrees: ")))
    n1 = float(input("Enter the refractive index of medium 1 [unitless]: ")) 

    if n1>n2:
        crit_angle = round(calc_crit_angle (n1,n2),1)
        if theta_in > crit_angle:
            print (f"For these two media, the critical angle is {crit_angle}\u00B0.")
            print (f"The incoming angle is larger than the critical angle.")
            print (f"This results in total internal reflection.")
            #n1>n2 condition with total internal reflection
        else: 
            theta_1 = (theta_in)
            theta_2 = calc_exit_angle (n1,n2,theta_in)
            theta2 = round(theta_2,1)
            d3 = float(round(calc_dist (d1,theta_1,d2,theta_2),1))
            print (f"For these two media, the critical angle is {crit_angle}\u00B0.")
            print (f"The light ray refracts with a leaving angle of {theta2}\u00B0.")
            print (f"The transverse distance traveled by the light ray is {d3} cm.")
            #n1>n2 with refraction of outgoing_angle. 
    else:
        theta_1 = (theta_in)
        theta_2 = calc_exit_angle (n1,n2,theta_in)
        theta2 = round(theta_2,1)
        d3 = float(round(calc_dist (d1,theta_1,d2,theta_2),1))
        print (f"The light ray refracts with a leaving angle of {theta2}\u00B0.")
        print (f"The transverse distance traveled by the light ray is {d3} cm.")
            #n2>n1 so everything refracts as normal. 
if __name__ == "__main__":
    main()
