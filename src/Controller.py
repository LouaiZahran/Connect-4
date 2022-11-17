from src import State, Minimax, TreePrinting
from src.GUI import GUI
from src.MinimaxWithoutPruning import MinimaxWithoutPruning
from src.Heuristic2 import Heuristic2

class Controller(object):

    def __init__(self):
        self.current_state = State()
        self.current_turn = True
        self.GUI = GUI()
        self.Heuristic = Heuristic2()
        self.Minimax = MinimaxWithoutPruning(self.Heuristic)
        self.TreePrinting = TreePrinting()

    def get_options(self):
        raise NotImplementedError

    def play_turn(self):
        column_number = None
        if self.current_turn:
            column_number = self.get_user_move()
        else:
            agent = self.get_agent_move()
            column_number = agent[0]
            self.TreePrinting.print_tree_console(agent[1])
            self.TreePrinting.print_tree_gui(agent[1])

        self.current_turn = not self.current_turn
        self.current_state.add_chip(column_number)
        self.GUI.display_grid(self.current_state.get_board(), column_number, animate=True)


    def get_user_move(self):
        return self.GUI.take_input()

    def get_agent_move(self):
        return self.Minimax.get_best_move(self.current_state, 3)


    #TODO
    def check_game_done(self):
        for column in range(7):
            if self.current_state.can_play(column):
                return False
        return True


    def start(self):
        game_done: bool = False
        while not game_done:
            self.play_turn()
            game_done = self.check_game_done()
            # if self.current_state.can_play(column_number):
            #     self.current_state.add_chip(column_number)
            #     self.GUI.display_grid(self.current_state.get_board(), column_number, animate=True)
            #     game_done = self.check_game_done()


if __name__ == "__main__":
    controller = Controller()
    controller.start()
