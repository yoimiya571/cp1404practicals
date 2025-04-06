"""
CP1404/CP5632 Practical
Unreliable Car class
"""
import random
from prac_09.car import Car


class UnreliableCar(Car):
    """Specialised version of a Car that includes reliability."""

    def __init__(self, name, fuel, reliability):
        """Initialise an UnreliableCar instance, based on parent class Car."""
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """Drive the car only if it is reliable enough, return distance driven."""
        if random.uniform(0, 100) < self.reliability:
            return super().drive(distance)
        return 0
