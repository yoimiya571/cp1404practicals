"""
CP1404/CP5632 Practical
Testing code using assert and doctest
"""

import doctest
from prac_06.car import Car


def repeat_string(s, n):
    """Repeat string s, n times, with spaces in between."""
    return " ".join([s] * n)


def is_long_word(word, length=5):
    """
    Determine if the word is as long or longer than the length passed in
    >>> is_long_word("not")
    False
    >>> is_long_word("supercalifrag")
    True
    >>> is_long_word("Python", 6)
    True
    """
    return len(word) >= length


def format_phrase_as_sentence(phrase):
    """
    Format a phrase as a sentence, starting with a capital and ending with a single full stop.
    >>> format_phrase_as_sentence("hello")
    'Hello.'
    >>> format_phrase_as_sentence("It is an ex parrot.")
    'It is an ex parrot.'
    >>> format_phrase_as_sentence("this is a test")
    'This is a test.'
    """
    phrase = phrase.strip()
    if not phrase.endswith('.'):
        phrase += '.'
    return phrase[0].capitalize() + phrase[1:]


def run_tests():
    """Run the tests on the functions."""
    # Test repeat_string
    assert repeat_string("Python", 1) == "Python"
    assert repeat_string("hi", 2) == "hi hi"

    # Test Car initialization
    car_default = Car()
    assert car_default._odometer == 0, "Car does not set odometer correctly"
    assert car_default.fuel == 0, "Car does not set fuel correctly by default"

    car_with_fuel = Car(fuel=10)
    assert car_with_fuel.fuel == 10, "Car does not set fuel correctly when specified"

    # Test is_long_word
    assert is_long_word("hello") == True
    assert is_long_word("hi") == False
    assert is_long_word("Python", 6) == True

    # Test format_phrase_as_sentence
    assert format_phrase_as_sentence("hello") == "Hello."
    assert format_phrase_as_sentence("It is an ex parrot.") == "It is an ex parrot."
    assert format_phrase_as_sentence("this is a test") == "This is a test."


# Enable doctest
doctest.testmod()

# Run tests
run_tests()