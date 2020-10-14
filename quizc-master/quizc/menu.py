from quizc.console.quiz_ui_handler import *
from quizc.MenuOptions import *


class Menu(object):
    MENU_PROMPT = "> "

    def __init__(self):
        self.car = ""
        self.quiz = None
        self.quiz_answers = None

    def show_main_menu(self):
        print("""
Quizc - A command quiz utility
======================================
1. Create quiz
2. Fill quiz
3. Show quiz
4. Exit
======================================
        """)

    def process(self):
        self.show_main_menu()
        option = input(self.MENU_PROMPT)
        should_exit = False
        numberofoptions(option)
        return should_exit
