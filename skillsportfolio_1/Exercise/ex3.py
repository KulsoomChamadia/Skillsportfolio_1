def main():
    # Define an empty dictionary for storing personal data
    Personal_Data = {}
    # Inquire about the user's name and hometown
    Personal_Data['Name'] = input(" Enter Your Name (First and Last):")
    Personal_Data['Hometown'] = input(" Enter Your Hometown:")
    # Authenticate the user's age input
    while True:
        Age_input = input("Enter Your Age: ")
        # Confirm that the input is a valid integer
        if Age_input.isdigit():
            # Interpret the input as an integer and save it in the dictionary
            Personal_Data['Age'] = int(Age_input) # Convert to integer
            break 
        else:
            # Ask the user to provide a valid number for their age
            print("Please Enter Valid Number for Your Age")
    # Print the results of the data collection       
    print("\n The Data")
    print("\nYour Information:")
    print(f"Name: {Personal_Data['Name']}\nHometown: {Personal_Data['Hometown']}\nAge: {Personal_Data['Age']}")

if __name__ == "__main__":
    main()
