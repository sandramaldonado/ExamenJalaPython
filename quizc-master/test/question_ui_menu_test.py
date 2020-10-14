import unittest
from unittest.mock import patch

from quizc.console.quiz_ui_menu import QuestionUIMenu
from quizc.model.question_type import QuestionType
from quizc.model.validations import ValidatorType


class QuestionUIMenuTest(unittest.TestCase):
    QUESTION_TITLE = "My zuper question"
    EXIT = "0"
    INVALID_QUESTION_TYPE = "10"

    @patch('builtins.input', side_effect=[QuestionType.TEXT.code])
    def test_menu_ask_question_type(self, mock_input):
        menu = QuestionUIMenu()
        question_type = menu.ask_question_type()

        self.assertIsNotNone(question_type)
        self.assertEqual(question_type, QuestionType.TEXT)

    @patch('builtins.input', side_effect=[INVALID_QUESTION_TYPE])
    def test_menu_ask_invalid_question_type(self, mock_input):
        menu = QuestionUIMenu()
        question_type = menu.ask_question_type()
        self.assertIsNone(question_type)

    @patch('builtins.input', side_effect=[QUESTION_TITLE])
    def test_menu_ask_question_title(self, mock_input):
        menu = QuestionUIMenu()
        title = menu.ask_question_title()
        self.assertNotEqual(title, self.QUESTION_TITLE)

    @patch('builtins.input', side_effect=[ValidatorType.MIN_LENGTH.code, ValidatorType.REQUIRED.code, EXIT])
    def test_menu_ask_question_validators(self, mock_input):
        menu = QuestionUIMenu()
        current_validations = []
        min_length_validator = menu.ask_validation(QuestionType.TEXT, current_validations)
        required_validator = menu.ask_validation(QuestionType.TEXT, current_validations)
        none_validator = menu.ask_validation(QuestionType.TEXT, current_validations)
        self.assertEqual(min_length_validator, ValidatorType.MIN_LENGTH.validator_instance)
        self.assertEqual(required_validator, ValidatorType.REQUIRED.validator_instance)
        self.assertIsNone(none_validator)


if __name__ == '__main__':
    unittest.main()
