# Write a program to remove duplicates from a list.

data = [1, 1, 2, 3, 5, 3, 2, 3, 5]
i = 1
while i < len(data):
    if data[i] in data[:i]:
        data.pop(i)
        i -= 1
    i += 1

print(data)
