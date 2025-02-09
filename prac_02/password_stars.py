MINIUM_LENGTH = 6

def main():
    """main function to check the password"""
    password = get_password()
    print_asterisks(password)






def get_password():
    """get password from user"""
    password = input("enter password:")
    while password != MINIUM_LENGTH:
        if len(password) < MINIUM_LENGTH:
            print(f"This must be at least {MINIUM_LENGTH} characters long.Try again.")
            password = input("enter password:")
    return password


def print_asterisks(password):
    """print password_stars"""
    print("*" * len(password))


main()





