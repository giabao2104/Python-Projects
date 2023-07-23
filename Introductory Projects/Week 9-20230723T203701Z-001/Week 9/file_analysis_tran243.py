"""
Author: Gia Bao Tran, tran243@purdue.edu
Assignment: 09.4 - File Analysis
Date: 11/06/2021

Description:
    This program input files and sort the content in alphabetical before outputting to four other files depending on the conditions set. 

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
import string
#fdsfjdslkf jsdklfjsdlkfjsdflksjdflskdjfsdlkfjs;odifjsdilfjsdifjsdijfsdifjsd;ifjsdoifjsdo;ifjsd;i
def main():
    file = open("xian_1.txt")
    file1 = open("xian_2.txt") #open and read files 
    x = file.read().lower().split()
    y = file1.read().lower().split()
    file.close()
    file1.close()

    with open ("xian_1_word_frequency.txt",'w+') as fileout: #write in output file
        for i in x: 
            set_x = set(x)
            sorted_x = sorted(set_x) #alphabetical order
            for j in sorted_x: 
                totaluniquex = x.count(i)
                fileout.write(f"{j}: {totaluniquex}\n") #print statement
    fileout.close()

    with open("xian_2_word_frequency.txt",'w+') as fileout1: #second file
        for k in y: 
            set_y = set(y) #put in alphabetical order
            sorted_y = sorted(y)
            for l in sorted_y: 
                totaluniquey = y.count(k)
                fileout1.write(f"{l}: {totaluniquey}\n")
    fileout1.close()#close file

    sorted_x = set(sorted_x)
    with open("common_words.txt","w+") as fileout2: #third file
        c = sorted_x.union(sorted_y)
        c = sorted(c)
        for n in c:  #test for the second 
            n = n.strip(string.punctuation)
            fileout2.write(f"{n}\n")
    fileout2.close()#close file

    neither = (set_x.difference(set_y))
    neither1 = (set_y.difference(set_x))
    list1 = sorted(set(neither.union(neither1)))
    with open ("eitherbutnotboth.txt","w+") as fileout3: #test for the third and final file
        for p in list1: 
            p = p.strip(string.punctuation) 
            fileout3.write(f"{p}\n")
    fileout3.close()#close file

if __name__ == '__main__':
    main()

    



