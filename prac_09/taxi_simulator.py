"""
CP1404/CP5632 Practical
Taxi Simulator Program
"""
from prac_09.taxi import Taxi
from prac_09.silver_service_taxi import SilverServiceTaxi

def main():
    """Simulate taxi operations."""
    taxis = [
        Taxi("Prius", 100),
        SilverServiceTaxi("Limo", 100, 2),
        SilverServiceTaxi("Hummer", 200, 4)
    ]
    current_taxi = None
    bill_to_date = 0.0

    print("Let's drive!")
    menu = "q)uit, c)hoose taxi, d)rive"
    print(menu)

    while True:
        choice = input(">>> ").lower()
        if choice == "q":
            break
        elif choice == "c":
            print("Taxis available:")
            for i, taxi in enumerate(taxis):
                print(f"{i} - {taxi}")
            try:
                taxi_choice = int(input("Choose taxi: "))
                current_taxi = taxis[taxi_choice]
            except (IndexError, ValueError):
                print("Invalid taxi choice")
        elif choice == "d":
            if current_taxi:
                try:
                    distance = float(input("Drive how far? "))
                    distance_driven = current_taxi.drive(distance)
                    trip_cost = current_taxi.get_fare()
                    bill_to_date += trip_cost
                    print(f"Your {current_taxi.name} trip cost you ${trip_cost:.2f}")
                except ValueError:
                    print("Invalid distance")
            else:
                print("You need to choose a taxi before you can drive")
        else:
            print("Invalid option")

        print(f"Bill to date: ${bill_to_date:.2f}")
        print(menu)

    print(f"Total trip cost: ${bill_to_date:.2f}")
    print("Taxis are now:")
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")

if __name__ == "__main__":
    main()
