import sys
from stats import get_wordcount, get_char_count

def main():
    args = sys.argv
    try:
        book_path = args[1]
    except Exception:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    
    book_text = get_book_text(book_path)    
    #print(book_text)
    book_wordcount = get_wordcount(book_text)
    print(f"{book_wordcount} words found in the document")
    char_count_dict = get_char_count(book_text)
    sorted_char_dict = sort_char_count_dict(char_count_dict)
    get_book_report(book_path,book_wordcount,sorted_char_dict)

def get_book_text (path_to_file):
    with open(path_to_file) as f:
        return f.read()
    
def sort_on(d):
    return d["num"]

def sort_char_count_dict(unsorted_char_count_dict):
    sorted_char_count = [
        {"char": k, "num": v}
        for k, v in unsorted_char_count_dict.items()
    ]
    
    sorted_char_count.sort(reverse=True, key=sort_on)
    return sorted_char_count

def get_book_report(book_path, word_count, sorted_char_count):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for ch in sorted_char_count:
        if ch['char'].isalpha() == True:
            print(f"{ch['char']}: {ch['num']}")
    print("============= END ===============")

main()
