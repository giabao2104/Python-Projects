"""
Author: Gia Bao Tran, tran243@purdue.edu
Assignment: 09.3 - Course Info
Date: 11/06/2021

Description:
    This program will use the concept of dictionaries to output the course information.
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
def get_course_data():
    dictionary = {'CS101': {'room':'3004','instructor':'Django','time':'9:00 a.m.'},
'CS102': {'room':'4501','instructor':'Idle','time':'10:00 a.m.'},
'CS103': {'room':'6755','instructor':'Rich','time':'11:00 a.m.'}, #create a nested dictionary
'NT110': {'room':'1244','instructor':'Marshal','time':'12:00 p.m.'},
'CM241': {'room':'1411','instructor':'Pickle','time':'2:00 p.m.'}}
    return (dictionary) #return dictionary

def main():
    Userinp = (input("Enter a course number: ")) #user input
    dictionary = get_course_data() # call function

    if Userinp in dictionary.keys():
        print (f"  The details for course {Userinp} are:")
        print (f"    Instructor: {dictionary[Userinp]['instructor']}")
        print (f"          Room: {(dictionary[Userinp]['room'])}") #access items within the dictionary
        print (f"          Time: {dictionary[Userinp]['time']}")

    else: 
        print (f"  {Userinp} is an invalid course number.") #if course does not exist

if __name__ == '__main__':
    main()