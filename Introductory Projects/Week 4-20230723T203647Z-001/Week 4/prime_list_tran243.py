"""
Author: Gia Bao Tran, tran243@purdue.edu
Assignment: 04.5 - Prime List
Date: 10/02/2021

Description:
    This program lists all the prime numbers up until a certain number inputted by the user
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
            if x % 2 == 0 and x!= 2 or x % 3 == 0 and x!=3 or x % 5 == 0 and x!=5 or x % 7 == 0 and x!=7 or x%11 == 0 and x!=11 or x%13 ==0 and x!=13 or x%17 == 0 and x!=17 or x%19==0 and x!=19 or x%29 == 0 and x!=29 or x%31 == 0 and x!=31 or x%41==0 and x!=41 or x%101 == 0 and x!=101 or x %353==0 and x!=353 or x%757==0 and x!=757:
                return False
            else: 
                return True
#come up with conditions for whether a number is prime or not (same as task 4)


#create a list to place all values
def main():
    list_of_primes = []
    x = int(input("Enter a positive integer: "))
    #user input
    for i in range (2,x+1):
        if is_prime(i) == True:
            list_of_primes.append(i)
    #for loop and append each prime number (determined by if statement) to the list of primes

    print (f"The primes up to {x} are: ", end = '')
    for i in list_of_primes:
        if i == list_of_primes[len(list_of_primes)-1]:
            print (i)
        else:
            print (i, end = ', ')
    #for loop so to separate using commas.
    #final print statement
if __name__ == "__main__":
    main()

    #y = ''.join(list_of_primes)