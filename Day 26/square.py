# Day 26: Create a program that uses a lambda function to square each element of a list.

lt = input("Enter List: ")

lt = [int(i) for i in lt.split()]

square_list = list(map(lambda x: x*x, lt))

print(f"List after squaring each element: {square_list}")
