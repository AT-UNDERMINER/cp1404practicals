"""
Damien Turner
CP1404 - Practical Solution
Program description: Program using an API to access Wikipedia
Estimate: 30 mins
Actual: TODO: Add time actual
"""

import wikipedia


def main():
    """Wikipedia search program that gets and prints title, summary and URL."""
    search_phrase = input("Enter page title: ").strip()

    while search_phrase != "":
        page = wikipedia.page(search_phrase, auto_suggest=False)
        print(page.title)
        print(page.summary)
        print(page.url)
        print()
        search_phrase = input("Enter page title: ").strip()

    print("Thank you.")


if __name__ == "__main__":
    main()
