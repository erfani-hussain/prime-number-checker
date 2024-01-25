# Prime number checker
# defining function
def prime_checker(number):
  
  is_prime = True
  
  for i in range(2, number):
    
    if number % i == 0:
      is_prime = False
      
  if is_prime:
    print(f"'{number}' is a prime number.")
  else:
    print(f"'{number}' is a composite number.")
    
# Input
print("Welcome to the Prime number checker application!")
n = int(input("Enter the number to check: "))
prime_checker(number=n)