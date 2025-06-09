"""
Damien Turner
CP1404 - Practical Solution
Program description: Memberwise Addition practice problem
"""

def add_memberwise(list1, list2):
    """Return a new list where each element is the sum of corresponding
    elements from list1 and list2. If one list is shorter, missing values
    are treated as zero.
    """
    len1 = len(list1)
    len2 = len(list2)
    max_len = len1 if len1 > len2 else len2
    result = []
    for i in range(max_len):
        v1 = list1[i] if i < len1 else 0
        v2 = list2[i] if i < len2 else 0
        result.append(v1 + v2)
    return result


def main():
    """Demonstrate add_memberwise with example inputs."""
    print(add_memberwise([1, 2, 3], [4, 5, 6]))       # Expected [5, 7, 9]
    print(add_memberwise([1, 2, 3], [1, 2, 3, 4]))   # Expected [2, 4, 6, 4]


if __name__ == "__main__":
    main()