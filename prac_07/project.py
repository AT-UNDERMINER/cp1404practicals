"""
Damien Turner
CP1404 - Practical Solution
Program description: Project class for Project Management Program
Estimate: 60 mins
Actual: TODO: Add time actual
"""


class Project:
    """Represent a project with attributes."""

    def __init__(self, name, start_date, priority, cost_estimate, completion_percentage):
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.cost_estimate = cost_estimate
        self.completion_percentage = completion_percentage
