import random

# Constants
NUMBERS_PER_PICK = 6
MIN_NUMBER = 1
MAX_NUMBER = 45

# Function to generate a single quick pick without using set() or sample()
def generate_quick_pick():
    quick_pick = []
    while len(quick_pick) < NUMBERS_PER_PICK:
        num = random.randint(MIN_NUMBER, MAX_NUMBER)
        if num not in quick_pick:
            quick_pick.append(num)
    return sorted(quick_pick)

# Ask user how many quick picks they want
number_picks = int(input("How many quick picks would you like to generate? "))

# Generate and display the quick picks
for _ in range(number_picks):
    quick_pick = generate_quick_pick()
    # Format the output to align the numbers neatly
    print(" ".join(f"{number:2}" for number in quick_pick))