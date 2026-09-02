name = input("What is your name?: ");
grade1 = float(input("Enter your Math grade: "));
grade2 = float(input("Enter your Programming grade: "));
grade3 = float(input("Enter your Database grade: "));
grade4 = float(input("Enter your Web Development grade: "));

average = (grade1 + grade2 + grade3 + grade4) / 4;

print("Hello " + name + "!");
print("Average: " + str(average));
print("Results: " + ("Passed" if average >= 75 else "Failed"));





