class InputHandler(object):
    @staticmethod
    def get_input_as_int(message):
        value = input(message)
        try:
            return int(value)
        except ValueError:
            return None

    @staticmethod
    def get_input(message):
        return input(message)


