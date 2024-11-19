
day_month = {
    "January": 31,
    "February": 28,  
    "March": 31, 
    "April": 30,    
    "May": 31,   
    "June": 30,    
    "July": 31,   
    "August": 31,    
    "September": 30,    
    "October": 31,   
    "November": 30,   
    "December": 31,
}


month = input("Enter the {month} ")

if month in day_month:
    
    if month == "February":
        is_leap_year = input("Is this year a leap year? (yes/no)")
        
        if is_leap_year.lower() == "yes":
            day_month["February"] = 29
        else:
            day_month["February"] = 28
            
    print(f"There are {day_month[month]} days in {month}")
else:
    print("Wrong month name.")
