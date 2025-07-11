from stats import count_words

with open("books/frankenstein.txt") as book:
    text = book.read()

num_words = count_words(text)

print(f"{num_words} words found in the document")

