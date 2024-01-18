# Write a function that accepts a string and calculates the number of uppercase and lowercase letters in it.

string = "ThIs Is A sAmPlE sTrInG"

upper_case = lower_case = 0

for char in string:
    if char.isupper():
        upper_case += 1
    elif char.islower():
        lower_case += 1

print(f"The given string is: '{string}' \nTotal number of lower case characters are: {lower_case} \nTotal number of "
      f"upper case characters are: {upper_case}")