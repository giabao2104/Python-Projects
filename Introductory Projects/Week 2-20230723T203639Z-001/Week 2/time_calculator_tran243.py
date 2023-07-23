"""
Author: Gia Bao Tran, tran243@purdue.edu
Assignment: 02.4 - Time calculator
Date: 09/19/2021

Description:
    This program will calculate the total number of days, hours, minutes and seconds when given the number of seconds.  

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
    x = int(input("Please enter a time in seconds: "))
    no_days = x // 86400 
    no_hours = (x - 86400*no_days) // 3600
    no_minutes = (x - 86400*no_days - 3600*no_hours) // 60
    no_seconds = (x - 86400*no_days - 3600*no_hours - 60*no_minutes) 

#set up calculations of days, hours, minutes & seconds.

    if x < 60: 
        print (f"  {x:,} seconds is less than one minute.")

    else:
        print (f"  {x:,} seconds is: ", end = "")
        if no_days:
            if no_hours or no_minutes or no_seconds:
                print (f"{no_days:,} day(s)" , end = "")
            else:
                print (f"{no_days:,} day(s).")
        
        if no_hours: 
            if no_days:
                if no_minutes or no_seconds:
                    print (", ", end = "")
                else:
                    print(" and ", end = "")
            print (f"{no_hours:,} hour(s)" , end = "")

        if no_minutes: 
            if no_days:
                if no_hours or no_seconds:
                    print (", ", end = "")
                else: 
                    print (" and ", end = "")
            print (f"{no_minutes:,} minute(s)" , end = "")

        if no_seconds:
            print (f" and {no_seconds:,} second(s)" , end = "")

        print ('.')

#set up so that the program doesn't print values that are 0. 
        if no_hours: 
            if no_days:
                if no_minutes or no_seconds:
                    print (", ", end = " ")
                else:
                    print (" and " , end = " ")
            print (f"{no_hours:,} hour(s)", end = " ")

        if no_minutes: 
            if no_days or no_hours:
                if no_hours or no_seconds:
                    print (", ", end = "")
                else:
                    print(" and", end = "")
            print (f"{no_minutes:,} minute(s)", end = "")



if __name__ == '__main__':
    main()
