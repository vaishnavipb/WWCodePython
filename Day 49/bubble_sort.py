# Day 49: Create a program that implements the bubble sort algorithm.
elements = [int(i) for i in input("Input a list\n").split()]

for i in range(0, len(elements)):
    for j in range(0, len(elements)-i-1):
        if elements[j] > elements[j+1]:
            elements[j], elements[j+1] = elements[j+1], elements[j]

print(f"Sorted array is : {elements}")