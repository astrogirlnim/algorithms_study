#19
def countingSundays(n):
    """
    Counting the number of sundays that fell on the first of the month up to year n.
    """
    mdays = [31,28,31,30,31,30,31,31,30,31,30,31]
    mleap = [31,29,31,30,31,30,31,31,30,31,30,31]
    y = 1900 # represents 1900
    day = 7 # represents monday

    sundays = 0

    while y <= 1900+n:
        day += 1
        if day > 7:
            day -= 7
            
        print("year=",y)
        # Leap year
        if y == 2000 or y % 4 == 0:
            print("leap_year")
            for j in mleap:
                # leap year
                if day == 7 and y > 1900:
                    sundays += 1

                # get the next first day
                day = j % 7 + day 

                if day > 7:
                    day -= 7
        else:
            for j in mdays:
                 # leap year
                if day == 7 and y > 1900:
                    sundays += 1

                # get the next first day
                day = j % 8 + day 

                if day > 7:
                    day -= 7
        y += 1


    print(sundays)

countingSundays(100)