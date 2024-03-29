# Day 42: Write a program that uses a try-except block to handle division by zero.

num1 = int(input("Pass number 1:"))
num2 = int(input("Pass number 2:"))

try:
    print(num1 / num2)
except ZeroDivisionError as zde:
    print(f"Division of {num1}/{num2} caused division by zero exception. Exception '{zde}' handled.")
except Exception as e:
    print(f"Unexpected exception {e}")
