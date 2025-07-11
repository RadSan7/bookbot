from sys import argv
from stats import count_words, get_sorted_characters

if len(argv) == 1:
    print("Usage: python3 main.py <path_to_book>")
    exit(1)

with open(argv[1]) as book:
    text = book.read()

num_words, letters = count_words(text)
sorted_letters = get_sorted_characters(letters)

print("============ BOOKBOT ============")
print(f"Analyzing book found at {argv[1]}")
print("----------- Word Count ----------")
print(f"Found {num_words} total words")
print("--------- Character Count -------")

for item in sorted_letters:
    print(f"{item['char']}: {item['num']}")

print("============= END ===============")