import math

from . import Minimax
from . import Heuristic


class MinimaxWithoutPruning(Minimax):

    def __init__(self, heuristic):
        self.__heuristic: Heuristic = heuristic

    def __min_function(self, state, maxDepth):
        return self.__min_function_util(state, -1, maxDepth)

    def __max_function(self, state, maxDepth):
        return self.__max_function_util(state, -1, maxDepth)

    def __min_function_util(self, state, best_index, maxDepth):
        if maxDepth <= 0:
            return self.__heuristic.get_score(state), best_index

        states = state.get_successor()
        if len(states) == 0:
            return self.__heuristic.get_score(state), best_index
        minV = math.inf
        i = 0
        for curr_state in states:
            v, i = self.__max_function_util(curr_state,best_index, maxDepth - 1)
            if v < minV:
                minV = v
                best_index = i
            i += 1

        return minV, best_index

    def __max_function_util(self, state, best_index, maxDepth):
        if maxDepth <= 0:
            return self.__heuristic.get_score(state), best_index

        states = state.get_successor()
        if len(states) == 0:
            return self.__heuristic.get_score(state) , best_index
        maxV = -math.inf
        i = 0
        for curr_state in states:
            v = self.__min_function_util(curr_state,best_index, maxDepth - 1)
            if maxV > v:
                maxV = v
                best_index = i
            i += 1

        return maxV, best_index

    pass
