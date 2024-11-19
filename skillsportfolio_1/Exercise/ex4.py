def main():
    
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
    
    valid_count = 0

    for country, capital in cap_name.items():
    
        user_result = input(f"what is the capital of {country}? ").strip()
        
        if user_result.lower() == capital.lower():
            print("You got it!")
            valid_count += 1 
        else: 
            print(f"Nope! the correct answer is {capital} ")

    print(f"\nYou got {valid_count} out of {len(cap_name)} correct!")
    
if __name__ == "__main__":
    main()
