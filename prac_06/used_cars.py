from prac_06.car import Car

def main():
    """Demo test code to show how to use Car class."""
    my_car = Car("My Car", 180)
    my_car.drive(30)
    print(f"Car has fuel: {my_car.fuel}")
    print(my_car)

    # New Car object: "limo"
    limo = Car("Limo", 100)
    limo.add_fuel(20)  # Adding 20 units of fuel
    print(f"Limo has fuel: {limo.fuel}")
    limo.drive(115)  # Attempt to drive 115 km
    print(limo)  # Print the limo details

main()