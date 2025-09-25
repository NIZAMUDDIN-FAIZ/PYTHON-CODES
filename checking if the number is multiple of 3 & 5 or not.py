num = int(input("Enter a number: "))

# checking if it multiple or not 
if (num % 3 == 0) and (num % 5 == 0):
    print(f"{num} is a multiple of both 3 and 5.")
else:
    print(f"{num} is NOT a multiple of both 3 and 5.")
