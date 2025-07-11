def count_words(text):    

    words = text.split()
    num_words = len(words)

    letters = {}

    for i in range(len(text)):
        char = text[i]
        if char.isalpha():
            char = char.lower()
        letters[char] = letters.get(char, 0) + 1
        
    return num_words, letters

def sort_on(item):
    return item["num"]

def get_sorted_characters(char_dict):
    sorted_list = []

    for char, count in char_dict.items():
        if char.isalpha():  # pomijamy np. przecinki, spacje itp.
            sorted_list.append({"char": char, "num": count})

    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list
    