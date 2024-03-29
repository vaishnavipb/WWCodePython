# Day 22: Create a program to find the second-largest element in a list.

n = input("Input a list\n")

input_list = [int(i) for i in n.split()]

if input_list[0] > input_list[1]:
    first, second = input_list[0], input_list[1]
else:
    first, second = input_list[1],  input_list[0]

for i in range(0, len(input_list)):
    if input_list[i] > first:
        second = first
        first = input_list[i]

print(f'The second largest number in the list is: {second}')
