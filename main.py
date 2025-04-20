from stats import get_num_words, dict_of_words

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents=f.read()
    return file_contents


def main():
    num_words=get_num_words(get_book_text("/home/krish/bootdevgo/bookbot/books/frankenstein.txt"))
    print(f"{num_words} words found in the document")
    print(dict_of_words(get_book_text("/home/krish/bootdevgo/bookbot/books/frankenstein.txt")))

main()