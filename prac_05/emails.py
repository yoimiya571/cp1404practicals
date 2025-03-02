"""

Estimate: 25 minutes
Actual:   35 minutes
"""

def extract_name(email):
    """Extracts the name from the email address."""
    name_part = email.split('@')[0]
    name = name_part.replace('.', ' ').title()  # Replace dots with spaces and capitalize
    return name

def main():
    """Main function to store emails and names."""
    email_dict = {}

    while True:
        email = input("Email: ")
        if email == "":
            break  # Stop if the user enters a blank email

        name = extract_name(email)  # Extract name from email
        confirm = input(f"Is your name {name}? (Y/n) ").strip().lower()

        if confirm != "" and confirm != "y":
            name = input("Name: ")  # Ask for the name if not confirmed

        email_dict[email] = name  # Store the email and name in the dictionary

    # Print the stored names and emails
    for email, name in email_dict.items():
        print(f"{name} ({email})")

if __name__ == "__main__":
    main()