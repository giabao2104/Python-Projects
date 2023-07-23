"""
Author: Gia Bao Tran, tran243@purdue.edu
Assignment: 08.6 - Step Counter
Date: 11/08/2021

Description:
    This program will use modules to give the user a math problem they need to solve

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

def main():
    print('The average steps taken each month were:') #original print statement

    with open("steps.txt") as file:
        f = file.readlines()
    totalsteps = []
    for x in f:
        totalsteps.append(int(x))
    months = []
    months.append(sum(totalsteps[0:31])/31)
    months.append(sum(totalsteps[31:59])/28)
    months.append(sum(totalsteps[59:90])/31)
    months.append(sum(totalsteps[90:120])/30)
    months.append(sum(totalsteps[120:151])/31)
    months.append(sum(totalsteps[151:181])/30)
    months.append(sum(totalsteps[181:212])/31)
    months.append(sum(totalsteps[212:243])/31)
    months.append(sum(totalsteps[243:273])/30)
    months.append(sum(totalsteps[273:304])/31)
    months.append(sum(totalsteps[304:334])/30)
    months.append(sum(totalsteps[334:365])/31) #append sum of total number of steps

    print(f"   January : {months[0]:.2f}") #print statements with to 2 decimal places.
    print(f"  February : {months[1]:.2f}")
    print(f"     March : {months[2]:.2f}")
    print(f"     April : {months[3]:.2f}")
    print(f"       May : {months[4]:.2f}")
    print(f"      June : {months[5]:.2f}")
    print(f"      July : {months[6]:.2f}")
    print(f"    August : {months[7]:.2f}")
    print(f" September : {months[8]:.2f}")
    print(f"   October : {months[9]:.2f}")
    print(f"  November : {months[10]:.2f}")
    print(f"  December : {months[11]:.2f}") #final print statements

if __name__ == "__main__":
    main()