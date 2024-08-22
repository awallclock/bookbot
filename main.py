def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = get_word_count(text)
    character_count = get_character_count(text)
    print(f"--- Begin report of {book_path} ---")
    print(f"{word_count} words found in document")
    dict_list = separate_dictionary(character_count)
    for i in range(0, len(dict_list)):
        print(
            f"The {dict_list[i]['character']} character was found {dict_list[i]['value']} times"
        )
    print("--- End report ---")


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
        if char.isalpha():
            char_dict[char] = char_dict.setdefault(char, 0) + 1
    return char_dict


def separate_dictionary(dictionary):
    dictionary_list = []
    for character in dictionary:
        value = dictionary[character]
        temp_dictionary = {}
        temp_dictionary["character"] = character
        temp_dictionary["value"] = value
        dictionary_list.append(temp_dictionary)

    def sort_on(dict):
        return dict["value"]

    dictionary_list.sort(reverse=True, key=sort_on)
    return dictionary_list


main()
