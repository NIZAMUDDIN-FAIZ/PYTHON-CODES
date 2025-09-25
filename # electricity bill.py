# electricity bill
units =-<= 100:
    amount = units * 5
elif units <= 200:
    amount = units * 7
else:
    amount = units * 10

print(f"Total amount to be paid: Rs {amount}")
 
