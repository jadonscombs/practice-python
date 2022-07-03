"""
Project: Generating Random Quiz Files

Description: You will generate randomly generated quizzes on US State
capitals, where for each question, a given state must be matched to
the proper capital.

Core operation(s):
- Create N different quizzes (for N students)
- Create 50 randomly ordered multiple-choice questions for each quiz
- Write the quizzes to N text files
- Write the answer keys to N text files

Functional requirements:
- Store states and their capitals in a dictionary
- Call open(), write(), and close() for the quiz & answer key text files
- Use random.shuffle() to randomize question order and multiple choice options

Other details:
- "states-capitals.txt" lists 1 <capital, state> pair per line
"""

import random
from datetime import datetime
import os


def generate_capitals(path: str = "states-capitals.txt") -> dict:
    """
    This function returns a dict of United States <state:capital> mappings.
    """

    capitals = {}
    with open(path, "r") as capitals_file:
        for line in capitals_file:

            # split comma-separated capital-state entry
            line = line.split(",")

            # first item is capital, second item is state
            capital = line[0].strip()
            state = line[1].strip()

            # add <state:capital> entry to <capitals>
            capitals[state] = capital

    # if capitals is empty or does not contain 50 entries, raise exception
    if (not bool(capitals)) or (len(capitals) != 50):
        raise RuntimeError("Error: malformed <capitals> dict.")

    return capitals


def generate_quiz_questions_answers(n_questions: int = 50):
    """
    Returns a 2-tuple of:
    1. a list of randomly-ordered multiple-choice questions
    2. an associated list of answers for the generated quiz
    """

    # retrieve capitals dict, shuffle order of the states
    capitals = generate_capitals()
    capital_values = list(capitals.values())
    states = list(capitals.keys())

    questions = []
    answers = []

    question_template = "{q_num}. What is the capital of {state}?\n"
    answer_template = "    {option_i}. {answer_i}\n"
    answer_key_template = "{question_num}. {correct_option}\n"
    abcd = "ABCD"
    correct_option_str = ""

    # create n multiple-choice questions
    for n in range(n_questions):

        # randomize order of states (used per question)
        random.shuffle(states)

        # states[n] gets the Nth state;
        # capitals[ states[n] ] gets the capital FOR the Nth state;
        correct_answer = capitals[ states[n] ]

        # 1. exclude the correct answer from the wrong answer selection
        # 2. get 3 other (wrong) answers for the current question
        # 3. re-add the correct answer back to the wrong answer selection
        #    for future iterations in this loop
        capital_values.remove(correct_answer)
        wrong_answers = random.sample(capital_values, 3)
        capital_values.append(correct_answer)

        # make list of answer options for current question
        answer_options = wrong_answers + [correct_answer]
        random.shuffle(answer_options)

        # create question string
        question = question_template.format(
            q_num=n+1,
            state=states[n]
        )
        for i in range(4):

            # append ith answer option
            question += answer_template.format(
                option_i=abcd[i],
                answer_i=answer_options[i]
            )

            # take note of correct option label
            if answer_options[i] == correct_answer:
                correct_option_str = abcd[i]

        # question string built, now add to list of questions
        question += "\n"
        questions.append(question)

        answers.append(
            # add formatted answer to list of answers
            answer_key_template.format(
                question_num=n+1,
                correct_option=correct_option_str
            )
        )

    # diagnostic line:
    #print(
    #    "[generate_quiz_questions_answers]\n"
    #    f"Total questions generated: {len(questions)}\n"
    #    f"Total answers generated: {len(answers)}\n"
    #)

    # return 2-tuple of question list and answer list
    return (questions, answers)


def create_quizzes_answers_folder() -> dict:
    """
    Helper function to create a quizzes and answers folder,
    with included timestamp.

    Returns created directory names.
    """

    # get current date and time
    now = datetime.now().strftime("%Y-%m-%d-%H.%M.%S")

    # create target directory paths
    target_quiz_dir = os.path.join(
        os.getcwd(),
        f"quizzes {now}"
    )
    
    target_answers_dir = os.path.join(
        os.getcwd(),
        f"answers {now}"
    )

    # create the quizzes folder
    if not os.path.isdir(target_quiz_dir):
        os.makedirs(target_quiz_dir)

    # create the answers folder
    if not os.path.isdir(target_answers_dir):
        os.makedirs(target_answers_dir)

    return {
        "quiz_directory": target_quiz_dir,
        "answers_directory": target_answers_dir
    }


def generate_quizzes(n_quizzes: int = 35, verbose: bool = False) -> None:
    """
    Core function to generate N quizzes.

    Creates a "quizzes" folder in the current dir. if one does not exist.
    """

    # create timestamped quizzes and answers folders before starting
    quiz_answers_paths = create_quizzes_answers_folder()
    quiz_dir = quiz_answers_paths["quiz_directory"]
    answer_dir = quiz_answers_paths["answers_directory"]

    # generate quizzes and answer keys
    for quiz_num in range(n_quizzes):

        # create and open quiz and answer key files
        quiz_filepath = os.path.join(
            os.getcwd(),
            quiz_dir,
            f"capitalsquiz{quiz_num + 1}.txt"
        )
        answer_filepath = os.path.join(
            os.getcwd(),
            answer_dir,
            f"capitalsquiz_answers{quiz_num + 1}.txt"
        )
        
        with (
            open(quiz_filepath, "w") as quiz,
            open(answer_filepath, "w") as answer_key
        ):
            
            # write out header for the quiz
            quiz.write("Name:\n\nDate:\n\nPeriod:\n\n")
            quiz.write(f"{' ' * 20}State Capitals Quiz (Form {quiz_num + 1})")
            quiz.write("\n\n")

            # retrieve generated quiz and answer key
            questions, answers = generate_quiz_questions_answers()

            # write questions to the quiz file
            for question in questions:
                quiz.write(question)

            # write answers to answer key file
            for answer in answers:
                answer_key.write(answer)

    if verbose:
        # TODO: diagnostic report on quiz and answer key files
        n_quiz_files = len(os.listdir(quiz_dir))
        n_answer_files = len(os.listdir(answer_dir))
        print(
            "[generate_quizzes] info:\n"
            f"Quiz directory: {quiz_dir}\n"
            f"Quiz answers directory: {answer_dir}\n"
            f"Total quiz files found: {n_quiz_files}\n"
            f"Total quiz answer files found: {n_answer_files}"
        )


if __name__ == "__main__":

    generate_quizzes()













            
            
