# create a dictionary of months and their respective number of days
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

# Ask the user to specify the month
month = input("Enter the {month} ")
# Validate if the input month is acceptable
if month in day_month:
    # Check if the year is a leap year for February
    if month == "February":
        # Ask the user whether it's a leap year
        is_leap_year = input("Is this year a leap year? (yes/no)")
       # Adjust the number of days in February as needed 
        if is_leap_year.lower() == "yes":
            day_month["February"] = 29
        else:
            day_month["February"] = 28
   # Output the number of days in the chosen month         
    print(f"There are {day_month[month]} days in {month}")
else:
    # Display an error message for invalid month input
    print("Wrong month name.")
