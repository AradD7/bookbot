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
