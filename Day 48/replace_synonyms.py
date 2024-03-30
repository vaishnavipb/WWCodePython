# Day 48: Create a program that replaces specific words in a text with their synonyms
from nltk.corpus import wordnet
import random


def synonym_replacer(text, word):
    synonyms = []

    for syn in wordnet.synsets(word):
        for l in syn.lemmas():
            synonyms.append(l.name())

    new_text = text.replace(word, random.choice(list(set(synonyms))))
    return new_text


text = input("Enter text: ")
replace = input("Enter word to replace: ")
print(synonym_replacer(text, replace))