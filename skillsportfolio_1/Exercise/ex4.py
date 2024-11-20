def main():
 # Initialize a dictionary with countries and capitals   
    cap_name = {
        "France": "Paris",
        "Pakistan": "Islamabad", 
        "Japan": "Tokyo",
        "Germany": "Berlin",
        "Australia": "Canberra",
        "Italy": "Rome",
        "Canada": "ottawa",
        "United Kingdom": "London",
        "Spain": "Madrid",
        "Argentina": "Buenos Aires",
        }
    # Prepare a counter to count correct responses
    valid_count = 0
# Loop over the dictionary and ask the user for the capitals of each country
    for country, capital in cap_name.items():
    # Collect the user's answer and eliminate surrounding whitespace
        user_result = input(f"what is the capital of {country}? ").strip()
    # Verify if the user's answer matches the correct capital  
        if user_result.lower() == capital.lower():
            # If the answer is right, print a success message and add to the correct answer tally
            print("You got it!")
            valid_count += 1 
        else: 
            # If the response is incorrect, provide the correct answer
            print(f"Nope! the correct answer is {capital} ")
# Print the overall score
    print(f"\nYou got {valid_count} out of {len(cap_name)} correct!")
    
if __name__ == "__main__":
    main()
