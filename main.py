from stats import get_num_words, dict_of_words
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents=f.read()
    return file_contents
if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def main():
    num_words=get_num_words(get_book_text(sys.argv[1]))
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    lod=dict_of_words(get_book_text(sys.argv[1]))
    for value in lod:
        print(f"{value["char"]}: {value["value"]}")
    print("============= END ===============")
main()