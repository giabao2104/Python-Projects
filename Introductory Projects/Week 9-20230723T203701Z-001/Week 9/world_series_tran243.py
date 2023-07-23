"""
Author: Gia Bao Tran, tran243@purdue.edu
Assignment: 09.2 - World Series
Date: 11/06/2021

Description:
    This program will use dictionary to output all the winner of the world series throughout the years and conditional statements to eliminate exceptions. 

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

def load_winners_data():
    file = open("WorldSeriesWinners.txt")
    data = file.readlines()
    file.close()

    teams = [] #initialisation of lists
    count = []

    for i in range (0,len(data)): #adding all teams name to the list
        x = data[i].strip("\n")
        teams.append(x)
    
    for j in teams:  #number of time a team appears in the list
        count.append(teams.count(j)) 

    team_win_count = dict(zip(teams,count)) #creation of dictionary
    year = []

    for k in range(1903,2021): #append the appropriate year
        if k == 1904 or k == 1994:
            continue
        else: 
            year.append(k)
    
    teamandyear = dict(zip(year,teams))
    return team_win_count, teamandyear

def main():
    yearseries = int(input("Enter a year in the range 1903 -- 2020: "))
    team_win_count, team_year = load_winners_data()

    if yearseries == 1904 or yearseries == 1994:
        print (f"  The World Series wasn't played in the year {yearseries}.")
    elif yearseries > 2020 or yearseries < 1903:  #eliminate years where there were no data available 
        print (f"  Data for the year {yearseries} is not included in this system.")
    else: 
        team_x = team_year[yearseries]
        total = team_win_count[team_x]
        print (f"  The {team_x} won the World Series in {yearseries}.")
        print (f"  They have won the World Series {total} times.")    #final print statements

if __name__ == '__main__':
    main()