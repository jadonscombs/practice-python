# Preface
This project is inspired by a prompt found in *Automate the Boring Stuff with Python* by Al Sweigart. I highly recommend reading the book even if you do not plan on learning Python, as there are many low- and high-level ideas to draw inspiration from and translate in your own applications.

This project also serves as a basis to test and practice with the built-in `unittest` module in Python.


# About
This application generates a certain number of quizzes (`N`), each with 50 randomly ordered multiple-choice questions to test a user's knowledge on United States capitals (50 questions --> 50 states).

# Usage
This project assumes you have Python 3.X installed. There are two core files that can optionally be run standalone:
- `quiz_generator_driver.py` (standalone driver script)
    - Generates (2) timestamped folders each time it is run:
        - one for a single set of unique quizzes
        - one for the associated answer keys for each quiz

- `test_quiz_generator.py` (standalone `unittest` script)
    - Can run with IDE or on command-line (in project root directory) with:
        - `python -m unittest discover [-v]` (assuming test filenames follow `"test*.py"` naming)
        - `python -m unittest test_quiz_generator [-v]`
    - Use `-v` for verbose output when running tests

# Future Work
Current work planned for future iterations include:
- Generate single folder to hold the two folders for (quiz set) and (answer keys)
