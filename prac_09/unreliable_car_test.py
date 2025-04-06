"""
CP1404/CP5632 Practical
Test Unreliable Car class
"""
from prac_09.unreliable_car import UnreliableCar

def main():
    """Test the UnreliableCar class functionality."""
    # Create cars with varying reliability
    reliable_car = UnreliableCar("Mostly Reliable", 100, 90)
    unreliable_car = UnreliableCar("Not Reliable", 100, 10)

    # Attempt to drive each car a few times
    for i in range(1, 6):
        print(f"Attempt {i}: Driving 20km")
        print(f"{reliable_car.name} drove {reliable_car.drive(20)}km")
        print(f"{unreliable_car.name} drove {unreliable_car.drive(20)}km")

    # Print final states
    print("\nFinal states:")
    print(reliable_car)
    print(unreliable_car)

if __name__ == "__main__":
    main()