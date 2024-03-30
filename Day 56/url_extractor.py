# Day 56: Create a function to extract all URLs from a given text using regular expressions.
import re

string = input("Input a string\n")

url_pattern = r'https?://\S+|www\.\S+'

# Find all matches of the pattern in the text
urls = re.findall(url_pattern, string)

[print(url) for url in urls]