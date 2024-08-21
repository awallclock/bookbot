def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = get_word_count(text)
    character_count = get_character_count(text)
    # print(f"{character_count}")
    # print(f"{word_count} words found in document")
    separate_dictionary(character_count)


def get_book_text(file):
    with open("books/frankenstein.txt") as f:
        return f.read()


def get_word_count(text):
    words = text.split()
    return len(words)


def get_character_count(book):
    char_dict = {}
    for char in book:
        char = char.lower()
        char_dict[char] = char_dict.setdefault(char, 0) + 1
    return char_dict


def separate_dictionary(dictionary):
    new_dictionary = {}
    for character in dictionary:
        value = dictionary[character]
        new_dictionary["character"] = character
        new_dictionary["value"] = value
    print(new_dictionary)
    return


main()
