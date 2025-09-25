# ask user for account balance and withdrawl ammount 

balance =  float(input("enter your balance"))
withdrawl = float(input("enter the withdrawl ammount"))

#check if the withdrawl ammount is multiple of 100
if withdrawl % 100 != 0:
    print("enter the ammount in multiple of 100. ")
    
#check if the withdrawl ammount is greater than balance 
elif withdrawl > balance :
    print("insufficient balance")
else:
    #perform withdrawl 
    balance -= withdrawl 
    print("Transaction sucessful.  ")
    print(f"Remaning balance: {balance}")