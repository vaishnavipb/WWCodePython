# Day 34: Write a Python program to merge two dictionaries.

n = input("Size of dictionary 1? \n")

dictionary1 = {}
for i in range(0, int(n)):
    key, value = input("Enter key, value pair: ").split()
    dictionary1[key] = value

n = input("Size of dictionary 2? \n")
dictionary2 = {}
for i in range(0, int(n)):
    key, value = input("Enter key, value pair: ").split()
    dictionary2[key] = value

for key, value in dictionary2.items():
    if key in dictionary1:
        dictionary1[key] = [dictionary1[key], value]
    else:
        dictionary1[key] = value

print(f'The concatenated dictionary is : {dictionary1}')
