# Import the math module for mathematical operations and the Image class from the PIL library for image processing.

import math
from PIL import Image

# Define a function 'find_divisors' that takes a number as input and returns a list of its divisors.
def find_divisors(num):
    divisors = []
    for i in range(1, int(math.sqrt(num)) + 1):
        if num % i == 0:
            divisors.append((i, num // i))
    return divisors

# Open a text file called 'input.txt' for reading and store its contents as a binary string.
with open('input.txt', 'r') as file:
    binary_string = file.read().strip()

# Calculate the length of the binary string.
length = len(binary_string)

# Find divisors for the available dimensions (factors of the length of the binary string).
divisors = find_divisors(length)

# Check if there are no valid dimensions found for the given text length.
if not divisors:
    print("No valid dimensions found for the given text length.")
else:
    # Display the available dimensions to the user.
    print("Available dimensions:")
    for dimensions in divisors:
        print(dimensions)

    # Ask the user to choose dimensions for the image (e.g., '256x256').
    user_choice = input("Enter dimensions (e.g., '256x256'): ")
    width, height = map(int, user_choice.split('x'))

    # Create a new image with dimensions specified by the user, using binary data from the text file.
    image = Image.new('1', (width, height))
    data = [int(bit) for bit in binary_string]
    image.putdata(data)

    # Save the image in the appropriate format (e.g., PNG) with the filename 'output.png'.
    image.save('output.png', format='PNG')
    print("Image saved as 'output.png'")  # Print a message confirming the image has been saved.
