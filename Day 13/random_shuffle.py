# Day 13: Write a program to shuffle the elements of a list randomly.
import random

input_list = input("Pass a list to shuffle elements randomly")

input_list = [int(i) for i in input_list.split()]

shuffle_list = random.sample(input_list, len(input_list))

print(input_list)
print(shuffle_list)