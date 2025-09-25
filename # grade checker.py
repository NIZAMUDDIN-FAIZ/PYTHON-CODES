# grade checker
marks = float(input("Enter your marks (0-100): "))
if marks < 0 or marks > 100:
        print("Marks should be between 0 and 100.")
elif marks < 35:
        print("Result: Fail")
elif 35 <= marks <= 59:
        print("Result: Pass")
elif 60 <= marks <= 84:
        print("Result: First Class")
else:  # marks >= 85
        print("Result: Distinction")


