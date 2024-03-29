# Day 31: Create a program that checks if a given string is a valid email address.

email = input("Input an email address\n")

if '@' in email[0:]:
    if '.' in email[email.index('@'):-1]:
        print(f"The email: '{email}' is valid")
    else:
        print(f"The email: '{email}' is invalid")
else:
    print(f"The email: '{email}' is invalid")
