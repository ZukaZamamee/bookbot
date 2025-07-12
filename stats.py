def get_wordcount(book_text):
    #Split text string into words, count words in resulting list)
    return len(book_text.split())

def get_char_count(book_text):
    char_count = {}

    #convert all text to lowercase
    lowercase_text = book_text.lower()

    #count each character
    for c in set(lowercase_text):
        char_count[c] = lowercase_text.count(c)
    
    return char_count

