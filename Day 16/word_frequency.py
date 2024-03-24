# Day 16: Write a function that counts the frequency of each word in a sentence.

sentence = input("Enter a sentence to check word frequency\n")

frequency_dict = {}
for word in sentence.split():
    frequency_dict[word] = frequency_dict.get(word, 0)+1

print("Here is the count:")
for word, frequency in frequency_dict.items():
    print('\t', word, frequency)