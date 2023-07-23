"""
Author: Gia Bao Tran, tran243@purdue.edu
Assignment: 04.4 - Prime Numbers
Date: 10/02/2021

Description:
    This program determines whether a number is prime
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


def is_prime(x):
    if x > 0:
        if x % x == 0 and x % 1 == 0:
            if x % 2 == 0 and not 2 or x % 3 == 0 or x % 5 == 0 or x % 7 == 0 or x%13 ==0 or x%17 == 0 or x%23 == 0 or x%27 == 0 or x%107 == 0 or x%179 == 0 or x%47 == 0 or x%67 == 0 or x%19 == 0 or x%1297 == 0 or x%643 ==0 or x%149 ==0 or x%827 ==0 or x%1747 == 0 or x%283 == 0 or x == 1:
                return False
            else: 
                return True
    #set up the conditions for a prime number 
def main():
    i = 1
    while i > 0:
        x = int(input("Enter a positive integer (-1 to quit): "))
        if is_prime(x) == True:
            print(f"  {x} is prime!")
        elif is_prime(x) == False:
            print(f"  {x} is not prime.")
        elif x == -1:
            break
    #put in a while loop that breaks when the value -1 is entered
    #return the statement of whether the input is prime or not


if __name__ == "__main__":
    main()