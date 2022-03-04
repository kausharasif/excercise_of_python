def countdays(month):
    if month == 1:
        print("Jan month has 31 days")
    elif month == 2:
        print("feb month has 29 days")
    elif month == 3:
        print("march month has 31 days")
    elif month ==4:
        print("april month has 30 days")
    elif month == 5:
        print("may month has 31 days")
    elif month == 6:
        print("june month has 30 days")
    elif month == 7:
        print("july month has 31 days")
    elif month ==8:
        print("aug month has 31 days")
    elif month ==9:
        print("sep month has 30 days")
    elif month == 10:
        print("oct month has 31 days")
    elif month == 11:
        print("nov month has 30 days")
    elif month == 12:
        print("dec month has 31 days")
    else:
        print("Please enter the value between 1-12")


month = int(input("Enter month in numbers"))
countdays(month)