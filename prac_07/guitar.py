class Guitar:
    """Represent a guitar with a name, year, and cost."""

    def __init__(self, name, year, cost):
        """Initialize a Guitar instance."""
        self.name = name
        self.year = year
        self.cost = cost

    def __repr__(self):
        """Return a string representation of a Guitar."""
        return f"{self.name} ({self.year}) : ${self.cost:,.2f}"

    def __lt__(self, other):
        """Compare guitars by their year (used for sorting)."""
        return self.year < other.year