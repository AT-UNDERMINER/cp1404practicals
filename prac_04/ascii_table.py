"""
CP1404/CP5632 - Practical
ASCII character and code lookup tool with aligned ASCII table display in user-defined columns.
"""

LOWER = 33
UPPER = 127


def main():
    """Run the ASCII lookup and table display program."""
    character = input("Enter a character: ")
    print(f"The ASCII code for {character} is {ord(character)}")

    # Use get_number to validate the code input
    number = get_number(LOWER, UPPER)
    print(f"The character for {number} is {chr(number)}")

    columns = int(input("Enter the number of columns to display: "))
    print_ascii_table(columns)


def print_ascii_table(columns):
    """Display ASCII table from LOWER to UPPER bounds with the given number of columns."""
    count = 0
    for code in range(LOWER, UPPER + 1):
        print(f"{code:3} {chr(code)}", end="    ")
        count += 1
        if count % columns == 0:
            print()
    if count % columns != 0:
        print()  # Ensure the final line ends with a newline


def get_number(lower, upper):
    """Get an integer from user between lower and upper inclusive, re-prompting on invalid input."""
    prompt = f"Enter a number ({lower}-{upper}): "
    value = None
    while value is None or value < lower or value > upper:
        try:
            value = int(input(prompt))
            if value < lower or value > upper:
                print(f"Please enter a number between {lower} and {upper}.")
        except ValueError:
            print("Please enter a valid number!")
    return value


if __name__ == "__main__":
    main()
