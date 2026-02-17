# Number Analyzer Program

# Ask user for input
number = int(input("Enter a number: "))

# Even or Odd
if number % 2 == 0:
    print("Even")
else:
    print("Odd")

# Positive, Negative, or Zero
if number > 0:
    print("Positive")
elif number < 0:
    print("Negative")
else:
    print("Zero")

# Prime check
if number <= 1:
    print("Not Prime")
else:
    is_prime = True
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            is_prime = False
            break

    if is_prime:
        print("Prime")
    else:
        print("Not Prime")
