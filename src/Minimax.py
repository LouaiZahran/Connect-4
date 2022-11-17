from typing import Tuple, Any

from . import State
from .Tree import Node
import abc


class Minimax(object):

    def get_best_move(self, current_state: State, depth: int) -> tuple[int, Any]:
        result, root = self.__max_function(current_state, depth)
        best_index=result[1]
        board1 = current_state.get_board()
        board2 = current_state.get_successor()[best_index].get_board()

        for i in range(7):
            j = 0
            while board1[j][i] != 0 and j < 6:
                j += 1
            if j < 6 and board2[j][i] != 0:
                return i, root

    @abc.abstractmethod
    def __min_function(self, state, maxDepth): pass

    @abc.abstractmethod
    def __max_function(self,state,maxDepth): pass
