name = input("What is your name?: ")
grade1 = float(input("Enter your Math grade: "))
grade2 = float(input("Enter your Programming grade: "))
grade3 = float(input("Enter your Database grade: "))
grade4 = float(input("Enter your Web Development grade: "))

average = (grade1 + grade2 + grade3 + grade4) / 4

print()
print("Hello", name)
print("Average:", average)

if average >= 75:
    print("Result: Passed")
else:
    print("Result: Failed")


if float(average) >= 95:
    print("1")
elif float(average) == 94:
    print("1.1")
elif float(average) == 93:
    print("1.2")
elif float(average) == 92:
    print("1.3")
elif float(average) == 91:
    print("1.4")
elif float(average) == 90:
    print("1.5")
elif float(average) == 89:
    print("1.6")
elif float(average) == 88:
    print("1.7")
elif float(average) == 87:
    print("1.8")
elif float(average) == 86:
    print("1.9")
elif float(average) == 85:
    print("2")
elif float(average) == 84:
    print("2.1")
elif float(average) == 83:
    print("2.2")
elif float(average) == 82:
    print("2.3")
elif float(average) == 81:
    print("2.4")
elif float(average) == 80:
    print("2.5")
elif float(average) == 79:
    print("2.6")
elif float(average) == 78:
    print("2.7")
elif float(average) == 77:
    print("2.8")
elif float(average) == 76:
    print("2.9")
elif float(average) == 75:
    print("3")
else:
    print("FAILED")

