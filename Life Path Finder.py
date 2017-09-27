#Ram Bastola
#Find a path number using person's date of birth

#months function
def monthss():

    #dictionary of months
    month = {"January":1, "Feburary": 2, "March" : 3, "April": 4, "May": 5, "June":6, "July":7,

             "August":8, "September": 9,"October":1, "November":11, "December":3
             }
    #asking for user's birth month
    month_input= input("enter the month you were born in! ")

    for x in month:
        if month_input ==x:
            mt = int(month[x])     # finds the month number.
            mt = int(mt)
            print ("You were born in month", mt)
    print(mt)
    return (mt)

#days function
def days():

     # asking user's day of birth

    day = input("Type in the day you were born in! ")
    day_count = int(0)
    if len(day) == 1:
        day_count = int(day)
        return day_count
        print(day_count)


    # add the digits from day
    if int(day) == 11 or int(day) == 22 or int(day)==33:
        day_count = int(day)
        return day_count
        print (day_count)
    else:
        day_count = int(day[0]) + int(day[1])
        #print(day_count)
        if day_count >= 10:
            day_count = str(day_count)
            day_count = int(day_count[0]) + int(day_count[1])
            day_count =  int(day_count)
            return(day_count)
            print(day_count)

        else:
            day_count=int(day_count)
            return day_count
            print(day_count)


    print ("You were born in day", day)

#function for years
def yearss():

    year= input("Type in the year you were born in!")
    print ("You were born in the year", year)
    # add the digits of year

    year_count = (int(year[0]) + int(year[1]) + int(year[2]) + int(year[3]))


    if int(year_count) == 11 or int(year_count) == 22 or int(year_count)== 33:
        year_count = int(year_count)
        return year_count
        print(year_count)

    else:
        year_count= int(year_count)
        if year_count >= 10:
            year_count = str(year_count)
            year_count = (int(year_count[0]) + int(year_count[1]))
            year_count = int(year_count)
            return year_count
            print (year_count)

        else:
            year_count = int(year_count)
            return year_count
            print(year_count)

#function that solves for the path number
def Pnumber(mt, day_count, year_count):


    path_number =(mt + day_count + year_count)
    path_number = int(path_number)

    if int(path_number) == 11 or int(path_number) == 22 or int(path_number)==33:
        path_number = int(path_number)
        return path_number
    else:

        if path_number >=10:
            path_number = str(path_number)
            path_number = int(path_number[0]) + int(path_number[1])
            return path_number
            print(path_number)

        else:
            path_number = path_number
            return path_number
            print(path_number,"check")


    print ("Your path number is", path_number)

#calling every functions inside the main()

def main ():

    mt = monthss()
    print (mt)
    day_count = days()
    print(day_count)
    year_count = yearss()
    print (year_count)

#print final path number
    print("Your path number is", Pnumber(mt, day_count, year_count))


main()
