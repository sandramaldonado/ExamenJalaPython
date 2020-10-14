from quizc.menu import Menu


def run():
    menu = Menu()
    should_exit = False
    while not should_exit:
        should_exit = menu.process()
