from quizc.console.quiz_ui_handler import *

quiz = None
quiz_answers = None


def one():
    quiz = QuizUIHandler.create_quiz()
    return quiz


def two():
        if quiz is None:
            print("No quiz available, you must create first a quiz")
        else:
            quiz_answers = QuizUIHandler.fill_quiz(quiz)
            return quiz


def three():
        if quiz_answers is None:
            print("No filled quiz available, you must create first a quiz")
        else:
            QuizUIHandler.show_quiz(quiz_answers)


def four():
        val = True
        return val


def numberofoptions(option):

        switcher = {
            1: one(),
            2: two(),
            3: three(),
            4: four()

        }

        return switcher.get(option)