def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    num_letters = letter_count(text)
    sorted_letters = sort_on(num_letters)
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    
    for letter, count in sorted_letters:
        print(f"The '{letter}' character was found {count} times")

    print("--- End report ---")

def letter_count(text):
    my_dict = {}
    
    for letter in text.lower():
        if letter.isalpha():  
            if letter not in my_dict:
                my_dict[letter] = 1
            else:
                my_dict[letter] += 1
    return my_dict

def sort_on(num_letters):
    return sorted(num_letters.items(), key=lambda x: x[1], reverse=True)  # Sort by frequency


def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()


main()