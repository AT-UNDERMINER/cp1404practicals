"""
Damien Turner
CP1404 - Practical Solution
Program description: Strings practice task
"""

# Collect entries
entries = []
entry = input("Enter a string (blank to finish): ")
while entry != "":
    entries.append(entry)
    entry = input("Enter a string (blank to finish): ")

# Determine repeats
repeated = []
for s in entries:
    if entries.count(s) > 1 and s not in repeated:
        repeated.append(s)

# Output results
if repeated:
    print("Strings repeated:", ", ".join(repeated))
else:
    print("No repeated strings entered.")
