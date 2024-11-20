def comfirm_odd_even(num):  
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
  # Ask the user for a number  
  num = int(input("type a number: "))  
  # Identify whether the number is even or odd  
  result = comfirm_odd_even(num)  
  # Display the output 
  print(result)  
  
if __name__ == "__main__":  
  main()
