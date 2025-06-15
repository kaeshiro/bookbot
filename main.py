import sys
from stats import get_num_words, get_num_char, sort_dict


def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path_to_book = sys.argv[1]
    contents = get_book_text(path_to_book)
    num_words = get_num_words(contents)
    chars_dict = get_num_char(contents)
    sorted_dict = sort_dict(chars_dict)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path_to_book}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for d in sorted_dict:
        if d["char"].isalpha():
            print(f"{d["char"]}: {d["num"]}")


main()
