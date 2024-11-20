def check_even_odd(num):  
  """  
  Determines if a number is even or odd.  
  
  Args:  
    num (int): The number to check.  
  
  Returns:  
    str: A message indicating whether the number is even or odd.  
  """  
  if num % 2 == 0:  
    return f"{num} is even."  
  else:  
    return f"{num} is odd."  
  
def main():  
  # Get the number from the user  
  num = int(input("Enter a number: "))  
  # Check if the number is even or odd  
  result = check_even_odd(num)  
  # Print the result  
  print(result)  
  
if __name__ == "__main__":  
  main()
