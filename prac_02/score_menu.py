"""Program to interact with scores using a menu."""

from score import determine_result


def main():
    """Run the menu program to interact with score-related functions."""
    score = get_valid_score()
    print_menu()
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "G":
            score = get_valid_score()
        elif choice == "P":
            result = determine_result(score)
            print(f"The result is: {result}")
        elif choice == "S":
            print_stars(score)
        else:
            print("Invalid choice")
        print_menu()
        choice = input(">>> ").upper()
    print("Farewell!")


def print_menu():
    """Print the main menu options."""
    print("\nMenu:")
    print("(G)et a valid score")
    print("(P)rint result")
    print("(S)how stars")
    print("(Q)uit")


def get_valid_score():
    """Get a valid score between 0 and 100 inclusive."""
    score = float(input("Enter score (0-100): "))
    while score < 0 or score > 100:
        print("Invalid score")
        score = float(input("Enter score (0-100): "))
    return score


def print_stars(score):
    """Print as many stars as the score (rounded to integer)."""
    print("*" * int(score))


if __name__ == "__main__":
    main()
