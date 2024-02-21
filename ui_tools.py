## Name: Eddie Wu
## Date: 2/20/2024
## Description: Functions for console UI menu with branching and validation

import os


## Presents main menu and calls appropriate functions based on user choice
#
def present_menu():
    # Constants for current directory, image options, and processing options
    DIRECTORY = os.getcwd()
    IMAGE_OPTIONS = ['laptop_photo.jpg', 'queen_mary.jpeg']
    PROCESSING_OPTIONS = ['Lighten/Darken', 'Channel Color', 'Invert Color', 'Flip 180',
                          'Add Blur', 'Detect Edges', 'Artist Choice']

    # Variable for user choice
    user_choice = ''

    # Loop to run program until sentinel is detected
    while user_choice.upper() != 'Q':
        # Prompt user to choose image to alter
        print("\nChoose an image to alter, or Q to quit: ")

        # Print choices for image options
        for i in range(len(IMAGE_OPTIONS)):
            print(f"{i + 1}) {IMAGE_OPTIONS[i]}")
        user_choice = input()

        # Save file name to variable
        file_name = IMAGE_OPTIONS[int(user_choice)]

        # Exit loop if user chose to quit
        if user_choice.upper() == 'Q':
            break

        # Prompt user to choose processing option
        print("\nChoose a processing option, or Q to quit: ")

        # Print choices for processing
        for i in range(len(PROCESSING_OPTIONS)):
            print(f"{i + 1}) {PROCESSING_OPTIONS[i]}")
        user_choice = input()
        if user_choice.upper() == 'Q':
            break

        processing_option = int(user_choice)
        print(f"You picked option {processing_option}")
        # Call appropriate processing function based on user choice


        # Prompt user to process another image or quit
        user_choice = input("\nProcess another image? (Y/N): ")
        if user_choice.upper() != 'Y':
            user_choice = 'Q'

    print("done")


def main():
    present_menu()

main()
