def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    num_words = number_of_words(text)
    num_chars = number_of_characters(text)
    list_dicts = list_of_dicts(num_chars)
    
    print(f"============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print(f"----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print(f"--------- Character Count -------")
                
    for item in list_dicts:
        ch = item["char"]
        if ch.isalpha():
            print(f"{item["char"]}: {item["num"]}")
    
def get_book_text(file_path):
    with open(file_path) as f:
        return f.read()

from stats import number_of_words
from stats import number_of_characters
from stats import list_of_dicts
import sys

main()
