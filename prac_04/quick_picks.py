"""
CP1404 - Practical
Quick picks lottery number generator.
"""

from random import randint

NUMBERS_PER_LINE = 6
MINIMUM = 1
MAXIMUM = 45


def main():
    """Quick picks number generator"""
    number_of_quick_picks = get_valid_quick_picks()

    for i in range(number_of_quick_picks):
        quick_pick = []
        for j in range(NUMBERS_PER_LINE):
            number = randint(MINIMUM, MAXIMUM)
            while number in quick_pick:
                number = randint(MINIMUM, MAXIMUM)
            quick_pick.append(number)
        quick_pick.sort()
        print(" ".join(f"{number:2}" for number in quick_pick))


def get_valid_quick_picks():
    """Get a valid quick pick integer"""
    # I wanted more practice with exceptions
    is_valid_input = False
    while not is_valid_input:
        try:
            number_of_quick_picks = int(input("How many quick picks? "))
            is_valid_input = True
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

    return number_of_quick_picks


if __name__ == "__main__":
    main()
