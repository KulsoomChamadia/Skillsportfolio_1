# Initialize the list of names  
names = ["Jake", "Zac", "Ian", "Ron", "Sam", "Dave"]  
# Ask the user to input the search term  
search_term = input("Type the name, and let’s see if we can find it! ")  
# Search for the search term in the list of names  
if search_term.lower() in [name.lower() for name in names]:  
    
    print(f"{search_term} is included on the list.")  
else:  
    print(f"{search_term} has ghosted the list, not found!")