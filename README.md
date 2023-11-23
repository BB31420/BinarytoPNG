# Binary to Image Converter
This Python script converts a binary string stored in a text file into an image. The script will display each available output dimension based on the input file character count. 

## Checking If Python is Installed
To check if Python is installed on your system, open a terminal (Command Prompt on Windows, Terminal on macOS and Linux) and run the following command:

```
python --version
```
If Python is installed, you will see its version displayed.

### Installing Dependencies
Before running the script, you need to install the Pillow library (PIL Fork), which is used for image processing.

Open a terminal or command prompt.

Install Pillow using pip:

```
pip install pillow
```
## Running the Script in Visual Studio Code
If you want to use Visual Studio Code (VS Code) to run the script, follow these steps:

### Download VS Code:

If you don't have VS Code installed, you can download it from the official website: https://code.visualstudio.com/.

### Open VS Code:



Click on "File" and select "Open Folder."
Navigate to the folder where you have the script file (binaryimagegen.py) and your input text file (input.txt).
Install the Python Extension in VS code (if not already installed):

If prompted, install the Python extension for Visual Studio Code. This extension provides enhanced Python support.


Open the (binaryimagegen.py) script in VS Code.
Click the "Run Python File in Terminal" button in the top-right corner of the script editor or use the menu "Run > Run without Debugging"

Note: You should have a folder containing the script saved as a .py file and the input file saved as .txt. The output images will be saved in this folder. After the script is ran, it will detect the available output dimensions & ask for your selection in this format "256x256" or "128x512" for example.


