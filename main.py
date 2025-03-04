import sys
from stats import get_num_words, get_character_count, sort_dict_list

def get_book_text():
    with open(sys.argv[1]) as f:
        file_contents = f.read()
        return file_contents


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        return sys.exit(1)
    corpus = get_book_text()
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    num_words = get_num_words(corpus)
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    word_dict = get_character_count(corpus)
    sorted_list = sort_dict_list(word_dict)
    for item in sorted_list:
        print(f"{item['char']}: {item['count']}")
    print("============= END ===============")
if __name__ == "__main__":
    main()