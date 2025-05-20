import sys
from stats import get_num_words, get_letter_count, sort_dict

# PATH = "/home/aapte/workspace/bookbot/books/frankenstein.txt"

def get_book_text(path:str):
    with open (path) as f:
        file_contents = f.read()
    return file_contents
    

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(f"Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        path_to_book = sys.argv[1]
    print(f"============ BOOKBOT ============")
    print(f"Analyzing book found at {path_to_book}")
    print(f"----------- Word Count ----------")
    print(get_num_words(get_book_text(path_to_book)))
    print(f"--------- Character Count -------")
    for k, v in sort_dict(get_letter_count(get_book_text(path_to_book))).items():
        print('%s: %i' % (k, v))
    print("============= END ===============")
    
