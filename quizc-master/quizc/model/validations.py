import datetime
from enum import Enum


class RequiredValidator(object):
    MESSAGE = "This question is required"

    def validate(self, value, condition_value, errors):
        if value == "":
            errors.append(self.MESSAGE)


class DateValidator(object):
    DATE_FORMAT = '%m/%d/%Y'
    MESSAGE = "The date format is invalid, it should have the format mm/dd/yyyy"

    def validate(self, value, condition_value, errors):
        try:
            datetime.datetime.strptime(value, '%d/%m/%Y')
        except ValueError:
            errors.append(self.MESSAGE)


class NumberValidator(object):
    MESSAGE = "The value must be a number please."

    def validate(self, value, errors):
        try:
            number = int(value)
            return number
        except ValueError:
            errors.append(self.MESSAGE)


class OnlyUpperCaseText(object):
    MESSAGE = "The value must be in Upper Case Please"

    def validate(self, value, errors):
        if value.isupper() is False:
            errors.append(self.MESSAGE)


class MinValidator(object):
    MESSAGE = "The value must be greater than {min_value}"

    def validate(self, value, condition_value, errors):
        if value < condition_value:
            errors.append(self.MESSAGE.format(min_value=condition_value))


class MinLengthValidator(object):
    MESSAGE = "The value length must be grater than {min_value}"

    def validate(self, value, condition_value, errors):
        if len(value) < condition_value:
            errors.append(self.MESSAGE.format(min_value=condition_value))


class MaxLengthValidator(object):
    MESSAGE = "The value length must be less than {max_value}"

    def validate(self, value, condition_value, errors):
        if len(value)>condition_value:
            errors.append(self.MESSAGE.format(max_value=condition_value))


class ValidatorType(Enum):
    REQUIRED = (1, RequiredValidator())
    DATE = (2, DateValidator())
    MIN = (3, MinValidator())
    MIN_LENGTH = (4, MinLengthValidator())
    NUMBER = (5, NumberValidator())
    MAX_LENGTH = (6, MaxLengthValidator())
    UPPERCASE = (7, OnlyUpperCaseText())

    def __init__(self, code, validator_instance):
        self.code = code
        self.validator_instance = validator_instance

    @staticmethod
    def get_validator(validator_code):
        for validator in ValidatorType:
            if validator.code == validator_code or str(validator.code) == validator_code:
                return validator.validator_instance
        return None
