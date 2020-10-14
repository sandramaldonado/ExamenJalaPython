class Question(object):
    def __init__(self, title, question_type, validations):
        self.title = title
        self.type = question_type
        self.validations = validations
        self.additional_data = []


class QuestionBuilder(object):
    def __init__(self, title, question_type):
        self.question_type = question_type
        self.title = title
        self.validations = []
        self.additional_data = []

    def add_validation(self, validation):
        if validation in self.validations:
            return False
        self.validations.append(validation)
        return True

    def build(self):
        question = Question(self.title, self.question_type, self.validations)
        if len(self.additional_data) > 0:
            question.additional_data = self.additional_data
        return question
