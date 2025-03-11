# Constant dictionary of color names and their hexadecimal codes
COLOR_NAME_TO_HEX = {
    "ALICEBLUE": "#f0f8ff",
    "ANTIQUEWHITE": "#faebd7",
    "AQUA": "#00ffff",
    "AZURE": "#f0ffff",
    "BEIGE": "#f5f5dc",
    "BISQUE": "#ffe4c4",
    "BLACK": "#000000",
    "BLUE": "#0000ff",
    "CORAL": "#ff7f50",
    "DARKKHAKI": "#bdb76b"
}

# User input loop
color_name = input("Enter a color name (or press Enter to quit): ").upper()
while color_name != "":
    if color_name in COLOR_NAME_TO_HEX:
        print(f"The hexadecimal code for {color_name} is {COLOR_NAME_TO_HEX[color_name]}.")
    else:
        print("Invalid color name.")
    color_name = input("Enter a color name (or press Enter to quit): ").upper()