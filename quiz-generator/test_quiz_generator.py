"""
This file contains unit tests to run on the Quiz Generator application (which
should be called "quiz_generator_driver.py").

STANDALONE: This unit testing file can be run as a standalone script, which
imports the quiz generator driver script.

This file is also a basis for experimenting with the built-in <unittest>
Python module.


TESTS TO RUN (PER FUNCTION):
[generate_capitals]
- test behavior when "states-capitals.txt" is not present
- are there 50 dict entries?
- confirm a few random state-capital entries for accuracy (assertion)
- test behavior when text file doesn't have commas
- test behavior when path doesn't exist or malformed


[generate_quiz_questions_answers]
- test behavior when N != 50
- confirm that input N matches output number of questions/answers also N
- test invalid argument behavior (N is not an int)


[create_quizzes_answers_folder]
- just run it and confirm output data type?


[generate_quizzes]
- test behavior when N != 35
- test invalid argument behavior (N is not an int)
- test invalid argument behavior (verbose is not bool)
- test non-verbose and verbose output
"""

import unittest
import quiz_generator_driver as quiz_prog


class TestGenerateCapitals(unittest.TestCase):

    def test_nonexistent_textfile(self):
        """
        Tests expected behavior when states-capitals text file is
        missing from local storage.
        """

        fake_path = "nonexistent_file_here.txt"
        self.assertRaises(
            FileNotFoundError, quiz_prog.generate_capitals, fake_path
        )

    def test_malformed_textfile(self):
        """
        Tests expected behavior when states-capitals text file does
        not contain all 50 state-capital pairs.
        """

        empty_file = "states-capitals-empty.txt"
        short_file = "states-capitals-short.txt"

        self.assertRaises(
            RuntimeError, quiz_prog.generate_capitals, empty_file
        )
        self.assertRaises(
            RuntimeError, quiz_prog.generate_capitals, short_file
        )

    def test_successful_dict_creation(self):
        """
        Standard test to confirm proper and successful creation of
        a dict of US <state:capital> mappings.
        """

        # generate state-capital dict with default filepath
        dict_result = quiz_prog.generate_capitals()

        # verify return type is dict
        self.assertIsInstance(dict_result, dict)
        
        # verify 50 entries exist
        self.assertEqual(len(dict_result), 50)

        # verify a couple test entries (information accuracy)
        state = "Washington"
        capital = "Olympia"
        self.assertEqual(dict_result[state], capital)

        
        



if __name__ == "__main__":
    unittest.main()















    


