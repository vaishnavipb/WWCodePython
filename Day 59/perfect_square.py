# Day 59: Create a function that checks if a number is a perfect square.

number = int(input("Enter a integer\n"))
if int(number ** 0.5) ** 2 == number:
    print(f"The number {number} is a perfect square.")
else:
    print(f"The number {number} is not a perfect square.")