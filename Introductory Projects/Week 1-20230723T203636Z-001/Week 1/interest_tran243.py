"""
Author: Gia Bao Tran, tran243@purdue.edu
Assignment: 01.2 - Interest
Date: 09/10/2021

Description:
    Calculating the value of a savings account after a number of years as a result of compound interest. Users will need to input the initial deposit, annual interest rate, how many times a year it is compounded and how many years it will earn interest. 

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
    
    print("Please enter the following quantities.")

    w = (float(input("  How much is the initial deposit? ")))
    x = (float(input("  What is the annual interest rate in percent? ")))
    xi = (x/100)
    #to find turn inputted number into a percentage
    y = (float(input("  How many times per year is the interest compounded? ")))
    z = (float(input("  How many years will the account earn interest? ")))
    #setting up variables with float (so users can input numbers) and input functions

    final_value = (round(w*(1+xi/y)**(y*z),2))
    #round answer to 2 decimal places 

    a = f"{final_value:,}"
    #comma separating thousands
    
    print (f"\nAt the end of {z} years, this account will be worth ${a}.")
    #final printing statement


    if __name__ == '__main__':
        main()

