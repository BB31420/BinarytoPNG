# Import necessary libraries
import binascii  # Import the binascii library for working with binary data
import math  # Import the math library for mathematical operations
from PIL import Image  # Import the Python Imaging Library (PIL) for image processing
import datetime  # Import the datetime library for handling date and time

# Define a function to find divisors of a number
def find_divisors(num):
    divisors = []  # Create an empty list to store pairs of divisors
    for i in range(1, int(math.sqrt(num)) + 1):
        if num % i == 0:
            divisors.append((i, num // i))  # Append a pair of divisors to the list
    return divisors  # Return the list of divisors

# Prompt the user for the file name they want to process
file_path = input("Enter the file name to process: ")

try:
    # Determine the file type based on the file extension
    if file_path.endswith('.bin'):
        # Handling binary file

        # Generate a unique output file name based on the current date and time
        output_file_path = f'output_{datetime.datetime.now():%Y%m%d%H%M%S}.txt'

        # Open the binary file for reading in binary mode
        with open(file_path, 'rb') as binary_file:
            binary_data = binary_file.read()  # Read the binary data from the file

        # Convert the binary data to a string of binary digits (0s and 1s)
        eight_bit_binary_data = ''.join(format(byte, '08b') for byte in binary_data)

        # Open the output file for writing
        with open(output_file_path, 'w') as output_file:
            output_file.write(eight_bit_binary_data)  # Write the binary data to the output file

        # Print a success message along with the name of the output file
        print(f"Successfully converted and saved to '{output_file_path}'")
    elif file_path.endswith('.txt'):
        # Handling text file and creating an image

        # Open the text file for reading
        with open(file_path, 'r') as file:
            binary_string = file.read().strip()  # Read the contents and remove leading/trailing whitespace

        length = len(binary_string)  # Get the length of the binary string
        divisors = find_divisors(length)  # Find divisors of the length

        if not divisors:
            print("No valid dimensions found for the given text length.")
        else:
            print("Available dimensions:")

            # Print the available dimensions (pairs of divisors)
            for dimensions in divisors:
                print(dimensions)

            # Prompt the user to enter dimensions (e.g., '256x256')
            user_choice = input("Enter dimensions (e.g., '256x256'): ")
            width, height = map(int, user_choice.split('x'))  # Split and convert to integers

            # Create a new binary image with the specified dimensions
            image = Image.new('1', (width, height))
            data = [int(bit) for bit in binary_string]  # Convert binary string to a list of integers
            image.putdata(data)  # Put the data into the image

            # Generate a unique filename for the image based on dimensions and current timestamp
            timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
            filename = f"output_{width}x{height}_{timestamp}.png"

            # Save the image in PNG format
            image.save(filename, format='PNG')

            # Print a message indicating that the image has been saved
            print(f"Image saved as '{filename}'")
    else:
        # Handle unsupported file types
        print("Unsupported file type. Please provide a .bin or .txt file.")
except FileNotFoundError:
    # Handle the case where the input file is not found
    print(f"File '{file_path}' not found.")
except Exception as e:
    # Handle other exceptions
    print(f"An error occurred: {str(e)}")
