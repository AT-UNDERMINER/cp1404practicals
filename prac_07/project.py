"""
Damien Turner
CP1404 - Practical Solution
Program description: Project class for Project Management Program
Estimate: 60 mins
Actual: 40 mins
"""


class Project:
    """Represent a project with attributes and helper methods."""

    def __init__(self, name, start_date, priority, cost_estimate, completion_percentage):
        """Construct a Project from given values."""
        self.name = name
        self.start_date = start_date  # datetime.date
        self.priority = priority
        self.cost_estimate = cost_estimate
        self.completion_percentage = completion_percentage

    def __str__(self):
        """Return a formatted string representation."""
        start_str = self.start_date.strftime("%d/%m/%Y")
        return (f"{self.name}, start: {start_str}, priority {self.priority}, "
                f"estimate: ${self.cost_estimate:.2f}, completion: {self.completion_percentage}%")

    def is_complete(self):
        """Return True if project is fully complete."""
        return self.completion_percentage >= 100

    def __lt__(self, other):
        """Enable sorting by priority (lower number = higher priority)."""
        return self.priority < other.priority
