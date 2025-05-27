MIN_LENGTH = 4


def main():
    """Get and print stars using functions"""
    password = get_password(MIN_LENGTH)
    print_stars(password)


def get_password(minimum_password_length):
    """Get user password that meets the minimum length."""
    password = input("Enter a password: ")
    while len(password) < minimum_password_length:
        print(f"Password must be at least {minimum_password_length} characters long.")
        password = input("Enter a password: ")
    return password


def print_stars(password_length):
    """Print stars using function"""
    print('*' * len(password_length))


if __name__ == "__main__":
    main()
