from src import State
from src.GUI import GUI


class Controller(object):

    def __init__(self):
        self.current_state = State()
        self.current_turn = False
        self.GUI = GUI()

    def get_options(self):
        raise NotImplementedError

    def play_turn(self):
        raise NotImplementedError

    def get_user_move(self):
        return self.GUI.take_input()

    def get_agent_move(self):
        raise NotImplementedError

    #TODO
    def check_game_done(self):
        return False

    def start(self):
        game_done: bool = False
        while not game_done:
            column_number = self.get_user_move()

            if self.current_state.can_play(column_number):
                self.current_state.add_chip(column_number)
                self.GUI.display_grid(self.current_state.get_board(), column_number, animate=True)
                game_done = self.check_game_done()


if __name__ == "__main__":
    controller = Controller()
    controller.start()
