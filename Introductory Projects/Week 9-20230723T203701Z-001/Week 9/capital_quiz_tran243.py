"""
Author: Gia Bao Tran, tran243@purdue.edu
Assignment: 09.1 - Capital Quiz
Date: 11/06/2021

Description:
    This program will quiz the user on the capital of each state in the US. 

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
import random 

def get_state_data():
    file = open("state_capitals.txt")
    l = file.readlines()
    capitals = []
    states = []
    for i in l:
        i1 = (i.split(",")[1].strip("\n").strip(" ")) #strip all spaces and punctations
        states.append(i1)
        capitals.append(i.split(",")[0])
    capquiz = dict(zip(states,capitals)) #creation of dictionary 
    file.close()
    return capquiz #return the dictionary 


def main():
    quiz = get_state_data()
    tally = 0 
    total = 0 
    indicator = 1
    while len(quiz) > 0: 
        state,capital = random.choice(list(quiz.items()))
        capital1 = capital.lower()
        userinp = input(f"What is the capital of {state} (enter 0 to quit)? ") #user input statement
       
        if userinp == str(0):
            break
        elif userinp == capital1 or userinp == capital: 
            total +=1 
            tally +=1
            print("  That is correct!")
            del quiz[state]
        else: #verify whether answers are correct 
            tally +=1 
            print ("  That is incorrect.")
            print(f"  The capital of {state} is {capital}.") 

    print(f"You answered {total} out of {tally} questions correctly.") #final print statements
if __name__ == '__main__':
    main()