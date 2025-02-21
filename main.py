import sys
from stats import word_count, letter_count

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_dir = sys.argv[1]
    with open(book_dir) as f:
        file_contents = f.read()
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {book_dir}")
        print("----------- Word Count ----------")
        print(f"found {word_count(file_contents)} total words")
        print("--------- Character Count -------")
        letters = letter_count(file_contents)
        for letter in sorted(letters):
            if letter.isalpha():
                print(f"{letter}: {letters[letter]}")
        print("============= END ===============")


main()
