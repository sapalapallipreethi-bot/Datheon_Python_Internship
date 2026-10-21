# Hangman Game Using Python

## About the Project
This is a terminal-based Hangman word guessing game developed using Python as Task 1 of the Datheon Python Programming Internship.

The player must guess a hidden word one letter at a time within six incorrect attempts.

## Features
- Random word selection
- ASCII Hangman drawing
- Displays hidden letters
- Tracks guessed letters
- Prevents duplicate guesses from reducing attempts
- Validates user input
- Displays win and game-over messages

## Technologies Used
- Python
- Python Standard Library (`random` module)

## How to Run
1. Install Python 3.
2. Download or clone this repository.
3. Open the project folder in a terminal.
4. Run the following command:

```bash
python hangman.py
```

## Sample Output
```text
WELCOME TO HANGMAN!
Word: P R O G R A M
Congratulations! You won!
The word was: PROGRAM
Thanks for playing!
```

## Learning Outcomes
- Practiced Python loops and conditional statements
- Learned sets and string manipulation
- Implemented random word selection
- Practiced input validation and game logic

## Internship
Datheon Python Programming Internship — Task 1

## Author
Preethi
## Task 3: Automated File Organizer & Cleanup Utility

### About the Project
This is a Python-based file organizer developed as Task 3 of the Datheon Python Programming Internship. It organizes files into separate folders based on their file extensions.

### Features
- Automatically organizes documents, images, videos, archives, and code files.
- Creates category folders automatically.
- Moves files using Python's `shutil` module.
- Prevents overwriting files with duplicate names.
- Handles permission and file operation errors.
- Displays a summary of successful and failed operations.
- Uses logging to display file movement details.

### Technologies Used
- Python 3
- `os`
- `shutil`
- `pathlib`
- `logging`

### How to Run
1. Install Python 3.
2. Open the project folder in a terminal.
3. Run the following command:

```bash
python organizer.py
```

4. Enter the folder path you want to organize when prompted.

### Sample Output

```text
AUTOMATED FILE ORGANIZER
INFO: Moved archive.zip -> Archives
INFO: Moved notes.txt -> Documents
INFO: Moved photo.jpg -> Images
INFO: Moved script.py -> Code

EXECUTION SUMMARY
Files relocated: 4
Failed operations: 0
```

### Learning Outcomes
- Practiced file and directory handling in Python.
- Learned to use `os.scandir()` and `shutil.move()`.
- Implemented exception handling and logging.
- Learned to prevent filename collisions.

### Internship
Datheon Python Programming Internship — Task 3

### Author
Preethi
