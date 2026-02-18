# Accept 5 marks
mark1 = float(input("Enter mark 1: "))
mark2 = float(input("Enter mark 2: "))
mark3 = float(input("Enter mark 3: "))
mark4 = float(input("Enter mark 4: "))
mark5 = float(input("Enter mark 5: "))

# Calculate average
average = (mark1 + mark2 + mark3 + mark4 + mark5) / 5

print("Average:", average)

# Determine grade
if average >= 80:
    print("Grade: A")
elif average >= 70:
    print("Grade: B")
elif average >= 60:
    print("Grade: C")
elif average >= 50:
    print("Grade: D")
else:
    print("Grade: F")