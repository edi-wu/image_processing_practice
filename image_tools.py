## Name: Eddie Wu
## Date: 2/20/2024
## Description: Functions for image processing

from PIL import Image


## Lighten or darken an image via multiplying RGB values by constant factor
# @param file_path - path to source image file (string)
# @param option - either "L" for lighten or "D" for darken (string)
# @param amount - percentage between 0-100 to adjust image by (integer)
#
def lighten_darken(file_path, option, amount):
    # Open image for processing
    with Image.open(file_path) as img:
        # Create black copy and load both pixel arrays
        altered_img = copy_image(img)
        source_pixels = img.load()
        altered_pixels = altered_img.load()
        # Nested loop to process pixel by pixel
        for x in range(img.width):
            for y in range(img.height):
                # Get source pixel and its RGB values
                old_pixel = source_pixels[x, y]
                # Adjust brightness accordingly to obtain new pixel
                new_pixel = adjust_brightness(old_pixel, option, amount)
                # Update altered pixel array
                altered_pixels[x, y] = new_pixel
        # Display altered image and prompt user to save or not
        show_and_save(altered_img, file_path)


## Create a copy of the provided image with all black color
# @param img - source image (PIL image object)
# @return PIL image object that has same size and mode as source
#
def copy_image(img):
    return Image.new(img.mode, img.size, color=(0, 0, 0))


## Calculates new RGB values based on lighten/darken amount
# @param pixel - RGB values of source pixel (tuple of three ints)
# @param option - 'L' or 'D' for lighten or darken operation (string)
# @param amount - percentage amount to adjust by (int)
# @return tuple of three ints for RGB values of altered pixel
#
def adjust_brightness(pixel, option, amount):
    ## To lighten, adjust each value by % difference between 255 and the lowest of the three values
    ## To darken, adjust each value by % difference between 0 and the highest of the three values
    # Convert pixel tuple to dict with RGB as keys
    pixel_dict = {'R': pixel[0], 'G': pixel[1], 'B': pixel[2]}
    if option == 'L':
        BOUND = 255
        # Get the lowest value from the three channels
        lowest_value = min(pixel)
        # Process to obtain adjustment
        distance = BOUND - lowest_value
        potential_adjustment = round(amount / 100 * distance)
        # Get the updated value within bounds
        lowest_value_updated = min(lowest_value + potential_adjustment, BOUND)
        # Get adjustment percentage for other values
        # NB: if distance is 0 i.e. lowest RGB value is already at BOUND, no adjust will occur
        actual_adjustment = lowest_value_updated - lowest_value
        increase_percentage = 0 if distance == 0 else actual_adjustment / distance
        # Update the lowest value in dict to the new value, and update other values using the percentage
        for (key, value) in pixel_dict.items():
            if value == lowest_value:
                pixel_dict[key] = lowest_value_updated
            else:
                pixel_dict[key] = round(value + (BOUND - value) * increase_percentage)

    elif option == 'D':
        # Same idea as lighten except adjust toward lower bound of 0
        BOUND = 0

        highest_value = max(pixel)
        distance = highest_value - BOUND
        potential_adjustment = round(amount / 100 * distance)

        highest_value_updated = max(highest_value - potential_adjustment, BOUND)
        actual_adjustment = highest_value - highest_value_updated
        decrease_percentage = 0 if distance == 0 else actual_adjustment / distance

        for (key, value) in pixel_dict.items():
            if value == highest_value:
                pixel_dict[key] = highest_value_updated
            else:
                pixel_dict[key] = round(value - (value - BOUND) * decrease_percentage)

    # Return the updated RGB values as a tuple
    return pixel_dict['R'], pixel_dict['G'], pixel_dict['B']


## Function to display altered image and prompt user to save
# @param img - altered image object for display (PIL image object)
# @param file_path - path to source image file (string)
#
def show_and_save(img, file_path):
    NAME_SUFFIX = '_saved'
    # Display image
    img.show()
    # Prompt user to choose to save
    user_choice = input("Do you want to save the altered image? (Y/N): ")
    if user_choice.upper() == 'Y':
        # Separate directory from file name (w/ extension)
        path_parts = file_path.rsplit("/", 1)
        directory, file_name = path_parts[0], path_parts[1]
        # Separate file name from extension
        name_and_extension = file_name.rsplit(".", 1)
        # Assemble new file path
        save_file_path = directory + "/" + name_and_extension[0] + NAME_SUFFIX + "." + name_and_extension[1]
        # Save the altered image
        img.save(save_file_path)

# def main():
    # show_and_save("test/i/o/image.jpeg")

# main()
