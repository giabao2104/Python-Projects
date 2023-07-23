"""
Author: Gia Bao Tran, tran243@purdue.edu
Assignment: 07.4 - Magic Square
Date: 10/25/2021

Description:
    This program verify whether the matrix entered will be a Lo-Shu square.

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

def print_square(list1):
    for i in list1:
        print(f"  {i[0]} {i[1]} {i[2]}") # print the square

def is_magic(list1):
    l1 = list1[0][:] + list1[1][:] + list1[2][:] #transform the list into a long list for easier manipulation
    for i in l1:
        l1.count(i)
        if l1.count(i) > 1: 
            return False

    if list1[0] and list1[1] and list1[2] and (list1[0][0] + list1[1][0] + list1[2][0]) == 15:
        if (list1[0][1] + list1[1][1] + list1[2][1]) and (list1[0][2]+list1[1][2]+list1[2][2])  == 15: 
            if (list1[0][0] + list1[1][1] + list1[2][2]) and (list1[2][0]+list1[1][1]+list1[0][2]) == 15: 
                return True #check through each index for the sum to be 15
            else:
                return False
        return False
    return False

def main():
    
    list1 = [[1,2,3],[4,5,6],[7,8,9]]#the original lists
    list2 = [[5,5,5],[5,5,5],[5,5,5]]
    list3 = [[4,9,2],[3,5,7],[8,1,6]]
    list4 = [[9,2,4],[1,6,8],[5,7,3]]

    print ("Your square is:")
    print_square(list1) # call the 1st function
    if is_magic(list1) == True: #and istrue(l1) == True: #conditional statement
        print ("It is a Lo Shu magic square!\n")
    else:
        print ("It is not a Lo Shu magic square.\n")

    print ("Your square is:")
    print_square(list2) # call the 2nd function
    if is_magic(list2) == True: #and istrue(l2) == True: #conditional statement
        print ("It is a Lo Shu magic square!\n")
    else:
        print ("It is not a Lo Shu magic square.\n")
    
    print ("Your square is:") 
    print_square(list3) # call the 3rd function
    if is_magic(list3) == True: #and istrue(l3) == True: #conditional statement
        print ("It is a Lo Shu magic square!\n")
    else:
        print ("It is not a Lo Shu magic square.\n")


#print functions and conditions
if __name__ == '__main__':
    main()