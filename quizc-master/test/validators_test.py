import unittest
from quizc.model.validations import *


class UtilsTest(unittest.TestCase):

    def test_factory_returns_date_validator(self):
        date_validator = ValidatorType.get_validator(ValidatorType.DATE.code)
        self.assertTrue(isinstance(date_validator, DateValidator), "Invalid date validator")

    def test_factory_returns_required_validator(self):
        required_validator = ValidatorType.get_validator(ValidatorType.REQUIRED.code)
        self.assertTrue(isinstance(required_validator, DateValidator), "The factory returned a wrong validator instance")

    def test_valid_date_validator(self):
        error = []
        required_validator = ValidatorType.get_validator(ValidatorType.DATE.code)
        required_validator.validate("12/21/2020", None, error)
        self.assertEqual(len(error), 0, "The date 12/21/2020 should be valid but currently it is marked as invalid")

    def test_invalid_date_validator(self):
        error = []
        required_validator = ValidatorType.get_validator(ValidatorType.DATE.code)
        required_validator.validate("2020/12/12", None, error)
        self.assertEqual(DateValidator.MESSAGE, error[0])

    def test_incomplete_date_validator(self):
        error = []
        required_validator = ValidatorType.get_validator(ValidatorType.DATE.code)
        required_validator.validate("2020", None, error)
        self.assertTrue(len(error) == 1)

    def test_factory_returns_min_validator(self):
        min_validator = ValidatorType.get_validator(ValidatorType.MIN.code)
        self.assertTrue(isinstance(min_validator, MinValidator))

    def test_min_validator(self):
        error = []
        min_validator = ValidatorType.get_validator(ValidatorType.MIN.code)
        min_validator.validate(101, 100, error)
        self.assertTrue(len(error) == 0)

    def test_value_less_than_expected(self):
        error = []
        min_validator = ValidatorType.get_validator(ValidatorType.MIN.code)
        min_validator.validate(99, 100, error)
        self.assertTrue(len(error) == 1)

    def test_factory_returns_min_length_validator(self):
        min_length_validator = ValidatorType.get_validator(ValidatorType.MIN_LENGTH.code)
        self.assertTrue(isinstance(min_length_validator, MinLengthValidator))

    def test_min_length_validator(self):
        error = []
        min_validator = ValidatorType.get_validator(ValidatorType.MIN_LENGTH.code)
        min_validator.validate("abcd", 3, error)
        self.assertTrue(len(error) == 0)

    def test_value_length_less_than_expected(self):
        error = []
        min_validator = ValidatorType.get_validator(ValidatorType.MIN_LENGTH.code)
        min_validator.validate("abc", 4, error)
        self.assertTrue(len(error) == 1)


if __name__ == '__main__':
    unittest.main()
