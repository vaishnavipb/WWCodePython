# Day 23: Write a program that checks if a key exists in a dictionary.

n = input("Size of dictionary? \n")

dictionary = {}
for i in range(0, int(n)):
    key, value = input("Enter key, value pair: ").split()
    dictionary[key] = value

key = input("Type in a key to check if it exists in a dictionary: ")

if key in dictionary:
    print("Key exists!!")
else:
    print("Key does not exist.")