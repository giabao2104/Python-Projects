def main():
    x = int(input("Please enter a number"))

    no_days = x // 86400 
    no_hours = (x - 86400*no_days) // 3600
    no_minutes = (x - 86400*no_days - 3600*no_hours) // 60
    no_seconds = (x - 86400*no_days - 3600*no_hours - 60*no_minutes) 

    if x < 60: 
        print (f"  {x} seconds is less than one minute.")
    
    else:
        print (f"{x} seconds is:", end = "")
        if no_days:
            print (f"{no_days} day(s)" , end = "")

        if no_hours: 
            print (f"{no_hours} hour(s)" , end = "")

        if no_minutes: 
            print (f"{no_minutes} minute(s)" , end = "")

        if no_seconds:
            print (f"{no_seconds} second(s)" , end = "")

        print ('.')

        if no_hours: 
            if no_days:
                if no_minutes or no_seconds:
                    print (", ", end = "")
                else:
                    print ("and" , end = "")
            print (f"{no_hours} hour(s)", end = "")
    
        if no_minutes: 
            if no_days or no_hours:
                if no_seconds:
                    print (", ", end = "")
                else: 
                    print ("and", end = "")
            print (f"{no_minutes} minute(s)", end = "")
        
        if no_seconds: 
            if no_days or no_hours or no_minutes:
                print (", ", end = "")
            else:
                print (", ", end = "")




if __name__ == '__main__':
    main()