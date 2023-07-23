"""
Author: Gia Bao Tran, tran243@purdue.edu
Assignment: 04.3 - Avg Grade
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
def determine_grade(score):
    if 91 <= score <= 100:
        return "A"
    elif 82 <= score < 91:
        return "B"
    elif 73 <= score < 82:
        return "C"
    elif 64 <= score < 73:
        return "D"
    else:
        return "F"

#if statements to return the letter grade depending on the scores


def get_valid_score():
    while 21==21:
        score = float(input("Enter a score: "))
        if 0 <= score <= 100:
            return score
#while true ask for an input and return score
        else:
            print ("  Invalid Input. Please try again.")
#invalid input 


def calc_average(input_list):
    ind_input = 0
    total = 0 
    while ind_input < len(input_list):
        total = total + input_list[ind_input]
        ind_input += 1
    average_score = (total / len(input_list))
    return average_score
#getting the sum of the list of entries and find the average

def main():
    input_list = []
    for i in range (0,5):
        studscore = get_valid_score()
        print (f"  The letter grade for {studscore:.1f} is " + str(determine_grade(studscore)) +".")
        input_list.append(studscore)
#for loop to call the function 5 times. 
#append each score into the list which will be passed into calc_average to calculate average score
    average = calc_average(input_list)
    grade = determine_grade(average)
#setting variables to call the 2 functions. 
    print()
    print ("Results:")
    print (f"  The average score is {average:.2f}.")
    print (f"  The letter grade for {average:.2f} is {grade}.")
#final print statements


if __name__ == "__main__":
    main()