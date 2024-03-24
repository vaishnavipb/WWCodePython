# Day 15: Create a program that checks if a year is a leap year.

# To determine whether a year is a leap year, follow these steps:
#
# If the year is evenly divisible by 4, go to step 2. Otherwise, go to step 5.
# If the year is evenly divisible by 100, go to step 3. Otherwise, go to step 4.
# If the year is evenly divisible by 400, go to step 4. Otherwise, go to step 5.
# The year is a leap year (it has 366 days).
# The year is not a leap year (it has 365 days).

n = int(input("Pass a year to check if it is leap year\n"))

if n % 4 == 0:
    if n % 100 == 0:
        if n % 400 == 0:
            print(f"Yes! {n} is leap year")
        else:
            print(f"{n} is not a leap year")
    else:
        print(f"Yes! {n} is leap year")
else:
    print(f"{n} is not a leap year")
