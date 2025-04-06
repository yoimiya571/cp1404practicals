"""
CP1404/CP5632 Practical
Band class
"""

class Band:
    """Band class to manage a group of musicians."""

    def __init__(self, name):
        """Initialise a Band with a name and an empty list of musicians."""
        self.name = name
        self.musicians = []

    def __str__(self):
        """Return a string representation of the Band, including its musicians."""
        return f"{self.name} ({', '.join(str(musician) for musician in self.musicians)})"

    def add(self, musician):
        """Add a musician to the band."""
        self.musicians.append(musician)

    def play(self):
        """Return a string showing each musician playing their first instrument, or needing one."""
        results = [musician.play() for musician in self.musicians]
        return "\n".join(results)