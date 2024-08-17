def main():
    book_path = "github.com/UrDadDrunk/Bookbot/books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_list = get_chars_list(text)
    chars_list.sort(reverse=True, key=sort_on)
    
    # Generowanie raportu
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document\n")
    
    for char_info in chars_list:
        if char_info["char"].isalpha():  # Wyświetl tylko litery
            print(f"The '{char_info['char']}' character was found {char_info['num']} times")
    
    print("--- End report ---")


def get_num_words(text):
    words = text.split()
    return len(words)


def get_chars_list(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    # Zamieniamy słownik na listę słowników zgodnych z formatem {"char": "a", "num": 5}
    chars_list = [{"char": k, "num": v} for k, v in chars.items()]
    return chars_list


def sort_on(char_dict):
    return char_dict["num"]


def get_book_text(book_path):
    with open(book_path) as f:
        return f.read()


main()
