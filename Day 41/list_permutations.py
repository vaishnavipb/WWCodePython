# Day41: Write a program that uses recursion to generate all permutations of a list.
import itertools


elements = [int(i) for i in input("Input a list\n").split()]
elements = list(itertools.permutations(elements))
print(elements)