def test_guitar():
    """Test the Guitar class methods."""
    guitar1 = Guitar("Gibson L-5 CES", 1922, 16035.40)
    guitar2 = Guitar("Another Guitar", 2013, 899.99)

    # Test get_age method
    print(f"{guitar1.name} get_age() - Expected 101. Got {guitar1.get_age()}")
    print(f"{guitar2.name} get_age() - Expected 10. Got {guitar2.get_age()}")

    # Test is_vintage method
    print(f"{guitar1.name} is_vintage() - Expected True. Got {guitar1.is_vintage()}")
    print(f"{guitar2.name} is_vintage() - Expected False. Got {guitar2.is_vintage()}")

# Run test for Guitar class
test_guitar()
