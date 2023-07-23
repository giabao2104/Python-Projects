def find_months():

    list_of_months = ["January", "February", "March", "April", "May", "June", "July", "August","September","October","November","December"]
    list_of_dates = [["September 1970"], ["March 1995"], ["April 2010"],["January 2013"],["September 2021"],["December 2023"],["October 2045"]]
    list_of_years = [1970, 1995, 2010, 2013, 2021, 2023, 2045]
    Futuredates = 0
    presentdate = 0
    pastdates = 0
    #sort by date
    #sort by month
    for years in list_of_years:
        if years > 2021:
            Futuredates += 1
        
        elif years == 2021:
            presentdate += 1
        
        else:
            pastdates += 1

#sort years in order 
    list_of_years.sort()
    for i in list_of_years:
        print (i)



find_months()