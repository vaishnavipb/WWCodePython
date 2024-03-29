# Day 57: Create a function that returns the key with the maximum value in a dictionary.

n = input("Size of dictionary? \n")

dictionary = {}
for i in range(0, int(n)):
    key, value = input("Enter key, value pair: ").split()
    dictionary[key] = int(value)

max_val, max_key = 0, None

for key, value in dictionary.items():
    if value > max_val:
        max_key = key
        max_val = value

print(f"The key {max_key} has the max value {max_val}")