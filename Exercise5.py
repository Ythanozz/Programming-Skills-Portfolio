dictionary = {            #defined the month numbers and their corresponding days in the dictionary
    "1" : 31,
    "2" : 29,
    "3" : 31,
    "4" : 30,
    "5" : 31,
    "6" : 30, 
    "7" : 31,
    "8" : 31,
    "9" : 30, 
    "10" : 31,
    "11" : 30,
    "12" :31,
    
    }

question=(input("Enter a month number from the calendar: "))

print(dictionary[question])       #prints the outcome of the users input from 1-12 which would be the days