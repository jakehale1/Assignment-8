import csv
import os

def display_menu():
    print("What file would you like to search for?:")
    print("    a) 60s-music file")
    print("    b) athletes file")
    print("    x) to exit")

def read_csv(file_path):
    data = []
    with open(file_path, newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            data.append(row)
    return data

# Provide the actual file paths for your system
file_path_60s_music = "60smusic.csv"
file_path_athletes = "athletes.csv"

data_60s_music = read_csv(file_path_60s_music)
athletes_data = read_csv(file_path_athletes)

def search_in_file(file_name, search_term):
    data = read_csv(file_name)
    matches = []
    for row in data:
        for item in row:
            if search_term.lower() in item.lower():
                matches.append(row)
                break  
    return matches

def main():
    while True:
        display_menu()
        choice = input("Enter your choice: ").strip().lower()

        if choice == 'x':
            print("Exiting...")
            break
        elif choice == 'a':
            selected_file = file_path_60s_music
        elif choice == 'b':
            selected_file = file_path_athletes
        else:
            print("Invalid choice. Please try again.")
            continue

        search_term = input(f"Enter the search term for {selected_file}: ").strip().lower()
        matches = search_in_file(selected_file, search_term)

        if matches:
            print(f"Your search term '{search_term}' exists in the {selected_file} file!")
            show_entries = input("Would you like to see the entries? (y or n): ").strip().lower()
            if show_entries == 'y':
                print(f"Here are all of the entries with the term '{search_term}':")
                for match in matches:
                    print(','.join(match))
        else:
            print(f"No matches found for '{search_term}' in {selected_file}.")

if __name__ == "__main__":
    main()

