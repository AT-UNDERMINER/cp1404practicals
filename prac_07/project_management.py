"""
Damien Turner
CP1404 - Practical Solution
Program description: Project Management Program
Estimate: 90 mins
Actual: TODO: Add time actual
"""

import datetime
from project import Project

DEFAULT_FILENAME = "projects.txt"


def main():
    """Run the project management menu loop."""
    projects = load_projects(DEFAULT_FILENAME)
    print(f"Loaded {len(projects)} projects from {DEFAULT_FILENAME}")
    choice = ""
    while choice != "q":
        display_menu()
        choice = input(">>> ").strip().lower()

        if choice == "l":
            filename = input("Filename: ")
            projects = load_projects(filename)
            print(f"Loaded {len(projects)} projects from {filename}")

        elif choice == "s":
            filename = input("Filename to save to: ")
            save_projects(filename, projects)
            print(f"{len(projects)} projects saved to {filename}")

        elif choice == "d":
            display_projects(projects)

        elif choice == "f":
            filter_projects_by_date(projects)

        elif choice == "a":
            new_proj = get_new_project()
            projects.append(new_proj)
            print(f"{new_proj.name} added")

        elif choice == "u":
            update_project(projects)

        elif choice == "q":
            save = input(f"Save to {DEFAULT_FILENAME}? (y/n): ").strip().lower()
            if save == "y":
                save_projects(DEFAULT_FILENAME, projects)
                print(f"{len(projects)} projects saved to {DEFAULT_FILENAME}")
            print("Thank you for using custom-built project management software.")

        else:
            print("Invalid choice; please select from the menu.")


def display_menu():
    """Display the available menu options."""
    print("- (L)oad projects")
    print("- (S)ave projects")
    print("- (D)isplay projects")
    print("- (F)ilter projects by date")
    print("- (A)dd new project")
    print("- (U)pdate project")
    print("- (Q)uit")


def parse_project_line(line):
    """Parse a tab-delimited line and return a Project."""
    parts = line.strip().split("\t")
    name = parts[0]
    start_date = datetime.datetime.strptime(parts[1], "%d/%m/%Y").date()
    priority = int(parts[2])
    cost = float(parts[3])
    completion = int(parts[4])
    return Project(name, start_date, priority, cost, completion)


def load_projects(filename):
    """Load projects from a tab-delimited file; return list of Project."""
    projects = []
    try:
        with open(filename, "r") as in_file:
            in_file.readline()  # skip header
            for line in in_file:
                if line.strip():
                    projects.append(parse_project_line(line))
    except FileNotFoundError:
        print(f"File '{filename}' not found. Starting with an empty list.")
    return projects


def save_projects(filename, projects):
    """Save a list of Project to a tab-delimited file (with header)."""
    with open(filename, "w") as out_file:
        out_file.write("Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage\n")
        for p in projects:
            date_str = p.start_date.strftime("%d/%m/%Y")
            out_file.write(f"{p.name}\t{date_str}\t{p.priority}"
                           f"\t{p.cost_estimate}\t{p.completion_percentage}\n")


def display_projects(projects):
    """Display incomplete and completed projects, each sorted by priority."""
    incomplete = sorted(p for p in projects if not p.is_complete())
    completed = sorted(p for p in projects if p.is_complete())
    print("Incomplete projects:")
    for p in incomplete:
        print(" ", p)
    print("Completed projects:")
    for p in completed:
        print(" ", p)


def get_project_date(project):
    """Return the start_date attribute (for sorting)."""
    return project.start_date


def filter_projects_by_date(projects):
    """Prompt for a date and display projects starting after it."""
    date_str = input("Show projects that start after date (dd/mm/yyyy): ")
    after_date = datetime.datetime.strptime(date_str, "%d/%m/%Y").date()
    # Collect matching projects
    filtered = []
    for p in projects:
        if p.start_date > after_date:
            filtered.append(p)
    # Sort by date using our named helper
    filtered.sort(key=get_project_date)
    # Display
    for p in filtered:
        print(p)


def get_new_project():
    """Prompt the user for project details and return a new Project."""
    name = input("Name: ")
    date_str = input("Start date (dd/mm/yyyy): ")
    start_date = datetime.datetime.strptime(date_str, "%d/%m/%Y").date()
    priority = int(input("Priority: "))
    cost = float(input("Cost estimate: $"))
    completion = int(input("Percent complete: "))
    return Project(name, start_date, priority, cost, completion)


def update_project(projects):
    """Let the user update completion % and/or priority of a chosen project."""
    for i, p in enumerate(projects):
        print(f"{i} {p}")
    choice = int(input("Project choice: "))
    project = projects[choice]
    print(project)
    comp = input("New Percentage: ")
    if comp:
        project.completion_percentage = int(comp)
    prio = input("New Priority: ")
    if prio:
        project.priority = int(prio)


if __name__ == "__main__":
    main()
