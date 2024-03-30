# Day 58: Create a function that converts a string to an integer and handles ValueError.

string = input("Enter a string that can be converted to int\n")

try:
    str_int = int(string)
    print(f"The input string {str_int} can be converted to int")
except ValueError as ve:
    print(f"The input string cannot be converted to int")
