"""
12. Create a function, is_palindrome, to determine if a supplied word is
the same if the letters are reversed.
"""
sample_word = 'ana'


def is_palindrome(word):
    reversed_word = word[::-1]
    if word == reversed_word:
        print(f'The word {word} is palindrome.')
    else:
        print(f'The word {word} is not palindrome.')


is_palindrome(sample_word)
