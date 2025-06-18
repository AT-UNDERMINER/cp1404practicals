"""
Damien Turner
CP1404 - Practical Solution
Program description: Wimbledon Winners Data Processor
Estimate: 26 minutes
Actual: 38 minutes
"""

FILENAME = "wimbledon.csv"


def main():
    """Display champion win counts and unique champion countries."""
    data = load_wimbledon_data(FILENAME)
    champion_to_wins = count_champions(data)
    print("Wimbledon Champions:")
    for champion, wins in sorted(champion_to_wins.items()):
        print(f"{champion} {wins}")

    countries = get_unique_countries(data)
    print(f"\nThese {len(countries)} countries have won Wimbledon:")
    print(", ".join(sorted(countries)))


def load_wimbledon_data(filename):
    """Load Wimbledon data from a CSV file and return list of rows (as lists of values)."""
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        lines = in_file.readlines()[1:]  # Skip header
        data = [line.strip().split(',') for line in lines]
    return data


def count_champions(data):
    """Count how many times each champion has won."""
    champion_to_wins = {}
    for row in data:
        champion = row[2]
        champion_to_wins[champion] = champion_to_wins.get(champion, 0) + 1
    return champion_to_wins


def get_unique_countries(data):
    """Get a set of unique champion countries."""
    countries = {row[1] for row in data}
    return countries


if __name__ == "__main__":
    main()
