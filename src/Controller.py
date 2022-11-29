from src import State, Minimax, TreePrinting
from src.GUI import GUI
from src.MinimaxWithPruning import MinimaxWithPruning
from src.MinimaxWithoutPruning import MinimaxWithoutPruning
from src.Heuristic1 import Heuristic1
from src.Heuristic2 import Heuristic2
from src.final_score import final_score
import easygui
import timeit


class Controller(object):

    def __init__(self):
        self.current_state = State()
        self.current_turn = True
        self.scorer = final_score()
        self.Heuristic = self.take_heuristic()
        self.Minimax = self.take_minimax(self.Heuristic)
        self.max_depth = self.take_max_depth()
        self.GUI = GUI()
        self.TreePrinting = TreePrinting()

    def take_heuristic(self):
        inp = easygui.buttonbox(
            "Select the heuristic",
            "Heuristic Selector",
            ["Heuristic 1", "Heuristic 2"]
        )

        if inp == "Heuristic 1":
            return Heuristic1()
        else:
            return Heuristic2()

    def take_minimax(self, heuristic):
        inp = easygui.buttonbox(
            "Select the minimax version",
            "Minimax Selector",
            ["With pruning", "Without pruning"]
        )

        if inp == "With pruning":
            return MinimaxWithPruning(heuristic)
        else:
            return MinimaxWithoutPruning(heuristic)

    def take_max_depth(self):
        inp = easygui.enterbox(
            "Enter the max depth of the minimax tree",
            "Depth Selector"
        )

        max_depth = int(inp)
        return max_depth

    def get_options(self):
        raise NotImplementedError

    def play_turn(self):
        column_number = None
        if self.current_turn:
            column_number = self.get_user_move()
        else:
            start = timeit.default_timer()
            agent = self.get_agent_move()
            stop = timeit.default_timer()
            print('Time: ', stop - start)

            column_number = agent[0]
            self.TreePrinting.print_tree_console(agent[1])
            self.TreePrinting.print_count()
            # self.TreePrinting.print_tree_gui(agent[1])

        self.current_turn = not self.current_turn
        self.current_state.add_chip(column_number)
        player_score, ai_score = self.scorer.get_final_score(self.current_state)
        self.GUI.display_grid(self.current_state.get_board(), column_number, animate=True, player_score=player_score, ai_score=ai_score)

    def get_user_move(self):
        return self.GUI.take_input()

    def get_agent_move(self):
        return self.Minimax.get_best_move(self.current_state, self.max_depth)

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
