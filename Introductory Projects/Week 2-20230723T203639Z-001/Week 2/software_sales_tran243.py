"""
Author: Gia Bao Tran, tran243@purdue.edu
Assignment: 02.2 - Software sales 
Date: 09/19/2021

Description:
    This program will ask the user for the amount of packages purchased and give them which discount range they are in.  

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
    x = int(input("How many packages will be purchased: "))

    nodiscount = (x*79) 
    discount1 = (x*79*0.9)
    discount2 = (x*79*0.8)
    discount3 = (x*79*0.7)
    discount4 = (x*79*0.55)
    no_discount = ("{:,.2f}").format(nodiscount)
    discount_1 = ("{:,.2f}").format(discount1)
    discount_2 = ("{:,.2f}").format(discount2)
    discount_3 = ("{:,.2f}").format(discount3)
    discount_4 = ("{:,.2f}").format(discount4)


#asking users for input & setting up calculations

    if 0 <= x <5:
        print ("  No discount applied.")
        print (f"  The total price for purchasing {x} packages is ${no_discount}.")
#set up conditions for different inputs 
    elif 5 <= x <= 24:
        print ("  10""%" " discount applied.")
        print (f"  The total price for purchasing {x} packages is ${discount_1}.")

    elif 25 <= x <= 49:
        print ("  20""%" " discount applied.")
        print (f"  The total price for purchasing {x} packages is ${discount_2}.")
    
    elif 50 <= x <= 99:
        print ("  30""%" " discount applied.")
        print (f"  The total price for purchasing {x} packages is ${discount_3}.")

    elif x >= 100:
        print ("  45""%" " discount applied.")
        print (f"  The total price for purchasing {x} packages is ${discount_4}.")

    else: 
        print ("  Invalid Input!")
#invalid negative value

if __name__ == '__main__':
    main()