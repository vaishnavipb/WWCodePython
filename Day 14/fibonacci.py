# Day 14: Write a program to print the first n numbers of a Fibonacci sequence.

n = int(input("Pass a number to print fibonacci sequence\n"))

n1, n2 = 0, 1

if n > 0:
    print(n1, sep=" ", end=" ")

i = 0
while i < n-1:
    n1, n2 = n2, n1 + n2
    print(n1, sep=" ", end=" ")
    i += 1
