 # Take weight 
weight = float(input("Enter your weight in kg: "))

if weight < 50:
    print("You are underweight.")
elif 50 <= weight <= 80:
    print("You have normal weight.")
else:
    print("You are overweight.")
