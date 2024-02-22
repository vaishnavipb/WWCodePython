# Write a program to check if a number is positive, negative, or zero.


if (number := -0.1) == 0:
    print(f"The given number '{number}' is zero")
elif number > 0:
    print(f"The given number '{number}' is positive")
else:
    print(f"The given number '{number}' is negative")
