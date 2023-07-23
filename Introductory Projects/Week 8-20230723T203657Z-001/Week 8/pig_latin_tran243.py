"""
Author: Gia Bao Tran, tran243@purdue.edu
Assignment: 08.1 - Pig Latin
Date: 10/02/2021

Description:
    This program calculates the average grade from a set of scores inputted
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
def pig(l): #user defined function
    list1 = []
    l = l.split() 
    for i in range (0,len(l)):
        if l[i] == "I" or l[i] == 'a': 
            text_new = l[i] + 'ay' # rule of i and a
            list1.append(text_new)
        else:
            first = l[i]
            second = first[:1].lower()
            first = first[1:]
            text_new = first + second + 'ay' #add the words back toether
            list1.append(text_new)
    list1 = [str(word) for word in list1]
    list1 = ' '.join(list1)
    list1 = list1.capitalize()
    return list1

def main():
    l = input("Enter a string: ")
    print(f"Pig latin: {pig(l)}") #final print statements

if __name__ == '__main__':
    main()