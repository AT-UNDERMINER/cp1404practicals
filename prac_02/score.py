"""Program to get a score from the user and print the corresponding status."""


def main():
    """Get number score and print status"""
    score = float(input("Enter score (0-100): "))
    print(determine_result(score))


def determine_result(score):
    """Assign status based on number score."""
    if score < 0 or score > 100:
        return "Invalid score"
    if score >= 90:
        return "Excellent"
    if score >= 50:
        return "Pass"
    return "Bad"


# Call the main function ONLY if the file is being run as
# a standalone program (Pg 304 Textbook)
if __name__ == "__main__":
    main()
