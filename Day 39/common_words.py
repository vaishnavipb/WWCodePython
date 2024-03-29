# Day 39: Write a program to find the most common words in a text file.

counter = {}
with open('sample.txt', 'r') as file:
    for line in file:
        for word in line.split():
            counter[word.lower()] = counter.get(word.lower(), 0) + 1

top_words = sorted(counter.items(), key=lambda x:x[1], reverse=True)

for word, count in top_words[:5]:
    print(f"'{word}' appeared {count} times.")