def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        file_name = f.name
    
    print_report(file_name, file_contents)

def count_words(text):
    word_count = 0
    for word in text.split():
        word_count += 1
    return word_count

def count_characters(text):
    lowered = text.lower()
    char_dict = {}
    for char in lowered:
        if char.isalpha():
            char_dict[char] = char_dict.get(char, 0) + 1
    return char_dict

def sort_on(dict):
    return dict["num"]

def characters_sorted_by_value(dict):
    sorted_list = []
    for char in dict:
        sorted_list.append({"char": char, "num": dict[char]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

def print_report (name, book):
    number_of_word = count_words(book)
    number_of_characters = count_characters(book)
    sorted_characters = characters_sorted_by_value(number_of_characters)
    

    print(f"--- Begin report of {name} ---")
    print("")
    print(f"Number of words: {number_of_word}")
    print("")
    for char in sorted_characters:
        print(f"The '{char['char']}' character was found {char['num']} times.")
    print("")
    print("--- End report ---")

if __name__ == "__main__":
    main()
