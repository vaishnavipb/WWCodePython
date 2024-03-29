# Day 29: Create a function that generates a random number between a given range.
import random


def generate_number(start, end):
    randint = random.randrange(start, end)
    return randint


start = int(input("Enter start range: "))
end = int(input("Enter end range: "))
print(f"Random number generated between given range is: {generate_number(start, end)}")
