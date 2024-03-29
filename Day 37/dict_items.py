# Day 37: Write a program to iterate through a dictionary and print its keys and values

n = input("Size of dictionary? \n")

dictionary = {}
for i in range(0, int(n)):
    key, value = input("Enter key, value pair: ").split()
    dictionary[key] = value

for key, value in dictionary.items():
    print(f"Key: {key}, value: {value}")
