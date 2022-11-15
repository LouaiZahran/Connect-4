from . import State
from . import Tree
import abc


class Minimax(object):

    def get_best_move(self, current_state: State, depth: int) -> int:
        result = self.__max_function(current_state, depth)
        best_index=result[1]
        tree=result[2]
        board1 = current_state.get_board()
        board2 = current_state.get_successor()[best_index]

        for i in range(7):
            j = 0
            while board1[j][i] != 0 and j < 6:
                j += 1
            if j < 6 and board2[j][i] != 0:
                return i ,tree

    @abc.abstractmethod
    def __min_function(self, state, maxDepth): pass

    @abc.abstractmethod
    def __max_function(self,state,maxDepth): pass
