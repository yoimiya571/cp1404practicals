"""
CP1404/CP5632 Practical
Recursion
"""


def do_it(n):
    """Do... it."""
    if n <= 0:
        return 0
    return n % 2 + do_it(n - 1)


def do_something(n):
    """Print the squares of positive numbers from n down to 0."""
    if n < 0:
        return
    print(n ** 2)
    do_something(n - 1)


def do_something_reverse(n):
    """Print the squares of numbers from 0 to n in reverse order."""
    if n < 0:
        return
    do_something_reverse(n - 1)
    print(n ** 2)


# Example test cases
print("do_it(5):", do_it(5))  # Should return sum of n % 2 from 5 to 0
print("do_something(4):")
do_something(4)  # Should print squares of 4, 3, 2, 1, 0
print("do_something_reverse(4):")
do_something_reverse(4)  # Should print squares in reverse order from 0 to 4