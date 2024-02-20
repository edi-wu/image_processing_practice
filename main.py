## Name: Eddie Wu
## Date: 2/20/2024
## Description: Main driver file for image processing exercise

from PIL import Image
import os


def main():
    # Obtain full path of source image
    directory = os.getcwd()
    file_name = 'queen_mary.jpeg'
    file_path = os.path.join(directory, file_name)

    # Open and display source image
    image = Image.open(file_path)
    image.show()

    # Inspect specs of source image
    print(f'Image size: {image.size}')
    print(f'Image mode; {image.mode}')

    # Create and save black image with same specs
    new_image = Image.new(image.mode, image.size, color=(0, 0, 0))
    new_image_path = os.path.join(directory, 'black_' + file_name)
    new_image.save(new_image_path)
    new_image.show()


if __name__ == "__main__":
    main()