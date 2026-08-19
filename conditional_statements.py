num = int(input("enter a number: "))

if num < 0:
    print("negative no.")
else:
    print("positive no.")

#nested if

marks = float(input("Enter your marks: "))

if marks >= 60:
    print("Congrats, you have passed the exam!")  # fixed: "you has" -> "you have"
    if marks >= 90:
        print("Your grade is A")
    elif 80 <= marks < 90:
        print("Your grade is B")
    elif 70 <= marks < 80:
        print("Your grade is C")
    else:
        print("Your grade is D")
else:
    print("You have failed, study hard next time")

# true-expression if condition else false-expression
print("Even") if num % 2 == 0 else print("odd")
