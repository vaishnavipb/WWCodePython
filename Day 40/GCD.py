# Day 40: Write a function to find the largest common divisor of two numbers using a function.

def gcd(num1, num2):
    start = num1 if num1 < num2 else num2
    while start > 0:
        if num1 % start == 0 and num2 % start == 0:
            print(f"{start} is the largest common divisor")
            break
        else:
            start -= 1


num1 = int(input("Pass number 1:"))
num2 = int(input("Pass number 2:"))

gcd(num1, num2)
