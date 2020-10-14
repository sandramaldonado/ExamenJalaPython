from quizc.model.question_type import QuestionType
from quizc.model.validations import ValidatorType
from quizc.model.question import QuestionBuilder
from quizc.model.question import Question
from quizc.model.quiz import Quiz


class QuestionUIMenu(object):
    MENU_PROMPT = "> "

    def ask_question_title(self):
        print("Type the question title")
        return input(self.MENU_PROMPT)

    def ask_question_type(self):
        print("Select a question to add")
        for question_type in QuestionType:
            message = "{code}. {question}"
            print(message.format(code=question_type.get_code(), question=question_type.name))

        question_code = input(self.MENU_PROMPT)
        return QuestionType.get_by_code(question_code)

    def ask_validation(self, question_type, validations):
        print("Select a validation to add")
        for validation in question_type.get_validations():
            if validation in validations:
                continue
            message = "{code}. {validation}"
            print(message.format(code=validation.code, validation=validation.name))
        print("0. To exit")
        validation_code = input(self.MENU_PROMPT)
        return ValidatorType.get_validator(validation_code)

    def ask_additional_data(self):
        additional_data = []
        while True:
            print("""Select an action:
1. Add question option
0. Exit""")
            option = input(self.MENU_PROMPT)
            if option == "0":
                if len(additional_data) == 0:
                    print("You must add at least one question option")
                    continue
                break
            elif option == "1":
                print("Option value")
                value = input(self.MENU_PROMPT)
                additional_data.append(value)

        return additional_data


    @staticmethod
    def handle_create_question() -> Question:
        menu = QuestionUIMenu()
        title = menu.ask_question_title()
        question_type = menu.ask_question_type()
        if question_type is None:
            return None

        builder = QuestionBuilder(title, question_type)

        if question_type.has_additional_data():
            builder.additional_data = menu.ask_additional_data()

        while True:
            validator = menu.ask_validation(question_type, builder.validations)
            if validator is None or not builder.add_validation(validator):
                break

        return builder.build()


class QuizUIMenu(object):
    MENU_PROMPT = "> "

    def ask_quiz_title(self):
        print("Type the quiz title")
        return input(self.MENU_PROMPT)

    def handle_create_quiz(self) -> Quiz:
        title = self.ask_quiz_title()
        quiz = Quiz(title)
        while True:
            print("""Select an option:
1. Add a new question
0. Finish""")
            option = input(self.MENU_PROMPT)
            if option == "0":
                break
            else:
                question = QuestionUIMenu.handle_create_question()
                quiz.add_question(question)
        return quiz
