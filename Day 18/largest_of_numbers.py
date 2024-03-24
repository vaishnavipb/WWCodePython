# Day 18: Create a program to find the largest among three numbers.

print("Enter three numbers as prompted to find largest number")
first = int(input("First number: "))
second = int(input("Second number: "))
third = int(input("Third number: "))

if first >= second and first >= third:
    print(f"{first} is the greatest!")
elif second >= first and second >= third:
    print(f"{second} is the greatest!")
else:
    print(f"{third} is the greatest!")
