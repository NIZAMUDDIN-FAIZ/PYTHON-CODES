# Input 
num = int(input("Enter a number: "))

# checking divisibility 
if (num % 4 == 0) and (num % 5 == 0):
    print(f"{num} is divisible by 4 and 5.")
else:
    print(f"{num} is NOT divisible by 4 and 5.")
