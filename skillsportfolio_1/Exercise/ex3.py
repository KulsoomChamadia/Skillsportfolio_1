def main():
    
    Personal_Data = {}
    
    Personal_Data['Name'] = input(" Enter Your Name (First and Last):")
    Personal_Data['Hometown'] = input(" Enter Your Hometown:")
    
    while True:
        Age_input = input("Enter Your Age: ")
        
        if Age_input.isdigit():
            Personal_Data['Age'] = int(Age_input) # Convert to integer
            break 
        else:
            print("Please Enter Valid Number for Your Age")
            
    print("\n The Data")
    print("\nYour Information:")
    print(f"Name: {Personal_Data['Name']}\nHometown: {Personal_Data['Hometown']}\nAge: {Personal_Data['Age']}")

if __name__ == "__main__":
    main()