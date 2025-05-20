# Broken Scores Solution

def main():
    """Get number score and print status"""
    score = float(input("Enter score: "))
    print(assign_status(score))


def assign_status(score):
    """Assign status based on number score"""
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Pass"
    else:
        return "Bad"


main()
