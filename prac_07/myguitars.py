import csv
from guitar import Guitar


def load_guitars(filename):
    """Load guitars from a CSV file and return a list of Guitar objects."""
    guitars = []
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            name, year, cost = row[0], int(row[1]), float(row[2])
            guitars.append(Guitar(name, year, cost))
    return guitars


def save_guitars(filename, guitars):
    """Save a list of Guitar objects to a CSV file."""
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        for guitar in guitars:
            writer.writerow([guitar.name, guitar.year, guitar.cost])


def main():
    """Main function to manage guitar collection."""
    filename = 'guitars.csv'

    # Load guitars from file
    guitars = load_guitars(filename)
    print("Guitars loaded from file:")
    for guitar in guitars:
        print(guitar)

    # Sort guitars by year and display
    guitars.sort()
    print("\nGuitars sorted by year:")
    for guitar in guitars:
        print(guitar)

    # Add new guitars
    print("\nAdd new guitars (leave name blank to finish):")
    while True:
        name = input("Name: ").strip()
        if not name:
            break
        year = int(input("Year: "))
        cost = float(input("Cost: "))
        guitars.append(Guitar(name, year, cost))

    # Save guitars back to file
    save_guitars(filename, guitars)
    print("\nGuitars saved to file.")
    for guitar in guitars:
        print(guitar)


if __name__ == "__main__":
    main()