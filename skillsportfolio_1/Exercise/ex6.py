def main():
    # Initialize the valid password
    valid_entry = "1214"
    # Define the maximum tries
    attempts = 0 
    # Configure the maximum tries allowed
    attempt_limit = 5
    # Create a while loop to keep asking for the password
    while attempts < attempt_limit:
        # Inquire for the user's password
        password = input("Password time! Curious if you remember it.")
        # Ensure the password is correct
        if password == valid_entry:
        # Print a message when the correct password is entered
            print("Look at you, remembering passwords! Welcome in.")
            
            break
        else:
        # Increment the attempt total
            attempts += 1
        # Let the user know how many attempts they have left
            attempts_left = attempt_limit - attempts
            
            print(f"Wrong! {attempts_left} tries before we panic.")
        # When the attempt limit is hit, update the user that the authorities are aware
    if attempts == attempt_limit:
        print("Oops! Out of tries. The digital detectives are coming.")
main()