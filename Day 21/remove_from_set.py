# Day 21: Create a program to remove a specific element from a set.

n = input("Input a set\n")

input_set = [int(i) for i in n.split()]

input_set = set(input_set)

remove_num = int(input("Enter a number to remove from the set\n"))

if remove_num in input_set:
    input_set.remove(remove_num)

print(f"Updated set: {input_set}")
