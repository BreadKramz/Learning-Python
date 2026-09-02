print("================================")
name = input("What is your name?: ")
print("================================")
print()
grade1 = float(input("Enter your Math grade: "))
grade2 = float(input("Enter your Programming grade: "))
grade3 = float(input("Enter your Database grade: "))
grade4 = float(input("Enter your Web Development grade: "))
print("================================")

average = (grade1 + grade2 + grade3 + grade4) / 4

print("Hello", name)
print("Average:", average)

if average >= 75:
    print("Result: Passed")
else:
    print("Result: Failed")

if float(average) >= 95:
    print("Grade: 1")
elif float(average) == 94:
    print("Grade: 1.1")
elif float(average) == 93:
    print("Grade: 1.2")
elif float(average) == 92:
    print("Grade: 1.3")
elif float(average) == 91:
    print("Grade: 1.4")
elif float(average) == 90:
    print("Grade: 1.5")
elif float(average) == 89:
    print("Grade: 1.6")
elif float(average) == 88:
    print("Grade: 1.7")
elif float(average) == 87:
    print("Grade: 1.8")
elif float(average) == 86:
    print("Grade: 1.9")
elif float(average) == 85:
    print("Grade: 2")
elif float(average) == 84:
    print("Grade: 2.1")
elif float(average) == 83:
    print("Grade: 2.2")
elif float(average) == 82:
    print("Grade: 2.3")
elif float(average) == 81:
    print("Grade: 2.4")
elif float(average) == 80:
    print("Grade: 2.5")
elif float(average) == 79:
    print("Grade: 2.6")
elif float(average) == 78:
    print("Grade: 2.7")
elif float(average) == 77:
    print("Grade: 2.8")
elif float(average) == 76:
    print("Grade: 2.9")
elif float(average) == 75:
    print("Grade: 3")
else:
    print("Grade: FAILED")
print("================================")