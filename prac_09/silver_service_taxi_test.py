"""
CP1404/CP5632 Practical
Test Silver Service Taxi class
"""
from prac_09.silver_service_taxi import SilverServiceTaxi

def main():
    """Test the SilverServiceTaxi class functionality."""
    # Create a SilverServiceTaxi instance
    fancy_taxi = SilverServiceTaxi("Limo", 100, 2)

    # Drive the taxi 18 km and print details
    fancy_taxi.drive(18)
    print(fancy_taxi)
    print(f"Fare: ${fancy_taxi.get_fare():.2f}")

    # Test with another SilverServiceTaxi
    hummer_taxi = SilverServiceTaxi("Hummer", 200, 4)
    hummer_taxi.drive(40)
    print(hummer_taxi)
    print(f"Fare: ${hummer_taxi.get_fare():.2f}")

if __name__ == "__main__":
    main()