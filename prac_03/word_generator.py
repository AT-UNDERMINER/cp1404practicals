"""
CP1404/CP5632 - Practical
Random word generator using a custom format string.
"""

import random
import string

VOWELS = "aeiou"
CONSONANTS = "".join([char for char in string.ascii_lowercase if char not in VOWELS])
LETTERS = string.ascii_lowercase


def main():
    """Main program to generate words from user-defined format."""
    choice = input("Do you want to enter your own word format? (y/n): ").lower()
    if choice == 'y':
        word_format = input("Enter word format (use % for consonant, # for vowel, * for any, or letters): ").lower()
    else:
        length = int(input("Enter length of word to randomly generate: "))
        word_format = generate_random_format(length)
        print(f"Random format used: {word_format}")

    word = generate_word(word_format)
    print(f"Generated word: {word}")


def generate_random_format(length):
    """Generate a random format string with %, #, and *."""
    symbols = ['%', '#', '*']
    return ''.join(random.choice(symbols) for _ in range(length))


def generate_word(format_string):
    """Generate a word based on the provided format string."""
    word = ""
    for symbol in format_string:
        if symbol == "%":
            word += random.choice(CONSONANTS)
        elif symbol == "#":
            word += random.choice(VOWELS)
        elif symbol == "*":
            word += random.choice(LETTERS)
        elif symbol.isalpha():
            word += symbol
        else:
            print(f"Unknown symbol '{symbol}' in format; skipping.")
    return word


if __name__ == "__main__":
    main()
