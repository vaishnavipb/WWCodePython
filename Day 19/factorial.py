# Day 19: Write a function to calculate the factorial of a number.

n = int(input("Enter a number to calculate factorial\n"))

temp = n
factorial = 1
while temp > 0:
    factorial = factorial*temp
    temp -= 1

print(f"The factorial of number {n} is: {factorial}")
