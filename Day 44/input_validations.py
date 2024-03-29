# Day 44: Write a program that reads an integer from the user and handles invalid inputs.

num1 = input("Input an integer: ")

try:
    if not isinstance(int(num1), int):
        print(f"The given input is not an integer.")
    else:
        print(f"The given input is an integer.")

except:
    print(f"The given input is not an integer.")