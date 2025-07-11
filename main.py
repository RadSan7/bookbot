from stats import count_words, get_sorted_characters

with open("books/frankenstein.txt") as book:
    text = book.read()

num_words, letters = count_words(text)

sorted_letters = get_sorted_characters(letters)

print("============ BOOKBOT ============")
print(f"Analyzing book found at books/frankenstein.txt")
print("----------- Word Count ----------")
print(f"Found {num_words} total words")
print("--------- Character Count -------")
for item in sorted_letters:
    print(f"{item['char']}: {item['num']}")
print("============= END ===============")
