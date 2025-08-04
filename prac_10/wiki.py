"""
Damien Turner
CP1404 - Practical Solution
Program description: Program using an API to access Wikipedia
Estimate: 30 mins
Actual: 20 mins
"""

import wikipedia


def main():
    """Wikipedia search program with exception handling and formatted output."""
    search_phrase = input("Enter page title: ").strip()

    while search_phrase != "":
        try:
            page = wikipedia.page(search_phrase, auto_suggest=False)
            print(page.title)
            print(page.summary)
            print(page.url)

        except wikipedia.exceptions.PageError:
            print(f'Page id "{search_phrase}" does not match any pages. Try another id!')

        except wikipedia.exceptions.DisambiguationError as e:
            print("We need a more specific title. Try one of the following, or a new search:")
            print(e.options)

        except Exception as e:
            print(f"An unexpected error occurred: {e}")

        print()
        search_phrase = input("Enter page title: ").strip()

    print("Thank you.")


if __name__ == "__main__":
    main()
