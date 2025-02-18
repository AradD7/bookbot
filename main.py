def main():
    book_dir = "books/frankenstein.txt"
    with open(book_dir) as f:
        file_contents = f.read()
        print(f"--- Begin report of {book_dir} ---")
        print(f"{word_count(file_contents)} words found in the document")
        letters = letter_count(file_contents)
        for letter in sorted(letters):
            if letter >= 'a' and letter <= 'z':
                print(f"The '{letter}' character was found {letters[letter]} times")
        print("--- End Report ---")

def word_count(s):
    words = s.split()
    return len(words)

def letter_count(s):
    s = s.lower()
    letter_counter = {}
    for letter in s:
        if letter in letter_counter:
            letter_counter[letter] += 1
        else:
            letter_counter[letter] = 1
    return letter_counter

main()
