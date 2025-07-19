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


def display_menu():
    """Display the available menu options."""
    print("- (L)oad projects")
    print("- (S)ave projects")
    print("- (D)isplay projects")
    print("- (F)ilter projects by date")
    print("- (A)dd new project")
    print("- (U)pdate project")
    print("- (Q)uit")
