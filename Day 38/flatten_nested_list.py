# Day 38: Write a program to flatten a nested list.

elements = [1, [2, [3], 4, 5, 6, [1, 2, 3]]]


# output = []
def get_elements(element, output):
    if isinstance(element, list):
        for i in range(0, len(element)):
            get_elements(element[i], output)
    else:
        output.append(element)
    return output


flatten_list = []
for i in range(0, len(elements)):
    flatten_list = get_elements(elements[i], flatten_list)

print(f"Flatten list is: {flatten_list}")
