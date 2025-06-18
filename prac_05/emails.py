"""
Damien Turner
CP1404 - Practical Solution
Program description: Email to Name Storage
Estimate: 25 minutes
Actual:   36 minutes
"""


def extract_name_from_email(email):
    """Extract a name from the email"""
    name_part = email.split('@')[0]
    name_parts = name_part.split('.')
    name = ' '.join(name_parts).title()
    return name


def get_email_name_mapping():
    """Get email-name pairs from user input."""
    email_to_name = {}
    email = input("Email: ")
    while email != "":
        name = extract_name_from_email(email)
        confirmation = input(f"Is your name {name}? (Y/n) ").lower()
        if confirmation not in ("", "y"):
            name = input("Name: ")
        email_to_name[email] = name
        email = input("Email: ")
    return email_to_name


def display_email_name_pairs(email_to_name):
    """Display the email-name pairs."""
    for email, name in email_to_name.items():
        print(f"{name} ({email})")


def main():
    """Run the email-name program."""
    email_to_name = get_email_name_mapping()
    display_email_name_pairs(email_to_name)


main()
