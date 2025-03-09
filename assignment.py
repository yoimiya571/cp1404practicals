"""
Name:Yuhao Guo
Date started:01.03.2025
GitHub URL:
"""


import csv
# Constants
SONGS_FILE = "songs.csv"
MENU = """Menu:
D - Display songs
A - Add new song
C - Complete a song
Q - Quit"""


def main():
    filename = "songs.csv"
    songs = load_songs(filename)
    welcome()

    while True:
        display_menu()
        choice = input(">>> ").strip().upper()

        if choice == 'D':
            display_songs(songs)
        elif choice == 'A':
            add_song(songs)
        elif choice == 'C':
            complete_song(songs)
        elif choice == 'Q':
            save_songs(filename, songs)
            print("Songs saved to file. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")



def welcome():
    print("Welcome to the Song List Manager by [Your Name]!")

def display_menu():
    print("\nMenu:")
    print("D - Display songs")
    print("A - Add a new song")
    print("C - Complete a song")
    print("Q - Quit")

def load_songs():
    """Load songs from the CSV file."""
    songs = []
    try:
        with open(SONGS_FILE, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                title, artist, year, learned = row
                songs.append([title, artist, int(year), learned == 'l'])
    except FileNotFoundError:
        print("No songs file found. Starting with an empty list.")
    return songs



def display_songs(songs):
    if not songs:
        print("No songs in the list.")
        return

def save_songs(filename, songs):
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        for song in songs:
            writer.writerow([song[0], song[1], song[2], 'l' if song[3] else 'u'])

    print("Song List:")
    for i, song in enumerate(songs, 1):
        title, artist, year, learned = song
        learned_status = "" if learned else "*"
        print(f"{i}. {learned_status} {title} - {artist} ({year})")

def add_song(songs):
    title = input("Enter the song title: ").strip()
    artist = input("Enter the artist: ").strip()
    while True:
        try:
            year = int(input("Enter the year: ").strip())
            if year < 0:
                raise ValueError
            break
        except ValueError:
            print("Invalid year. Please enter a positive integer.")



def complete_song(songs):
    unlearned_songs = [song for song in songs if not song['learned']]
    if not unlearned_songs:
        print("No more songs to learn!")
        return

    display_songs(unlearned_songs)
    while True:
        try:
            song_num = int(input("Enter the number of the song to mark as learned: ").strip())
            if 1 <= song_num <= len(unlearned_songs):
                break
            else:
                print("Invalid number. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    selected_song = unlearned_songs[song_num - 1]
    selected_song['learned'] = True
    print(f"{selected_song['title']} by {selected_song['artist']} marked as learned.")



if __name__ == "__main__":
    main()