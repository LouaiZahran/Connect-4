import math

from . import Minimax
from . import Heuristic


class MinimaxWithPruning(Minimax):
    def __init__(self, heuristic):
        self.__heuristic: Heuristic = heuristic

    def __min_function(self, state, maxDepth):
        self.__min_function_alpha_beta_util(state, -1, -math.inf, math.inf, maxDepth)

    def __max_function(self, state, maxDepth):
        self.__max_function_alpha_beta_util(state, -1, -math.inf, math.inf, maxDepth)

    def __min_function_alpha_beta_util(self, state, best_index, alpha, beta, maxDepth):
        if maxDepth <= 0:
            return self.__heuristic.get_score(state), best_index

        states = state.get_successor()
        if len(states) == 0:
            return self.__heuristic.get_score(state)
        minV = math.inf
        i = 0
        for curr_state in states:
            v = self.__max_function_alpha_beta_util(curr_state, best_index, alpha, beta, maxDepth - 1)
            if v < minV:
                minV = v
                best_index = i
            beta = min(beta, minV)
            if (beta <= alpha):
                return minV, best_index

        return minV, best_index

    def __max_function_alpha_beta_util(self, state, best_index, alpha, beta, maxDepth):
        if maxDepth <= 0:
            return self.__heuristic.get_score(state)

        states = state.get_successor()
        if len(states) == 0:
            return self.__heuristic.get_score(state)
        maxV = -math.inf
        i = 0
        for curr_state in states:
            v = self.__min_function_alpha_beta_util(curr_state, best_index, alpha, beta, maxDepth - 1)
            if maxV > v:
                maxV = v
                best_index = i
            i += 1
            alpha = max(alpha, maxV)
            if (beta <= alpha):
                return maxV, best_index

        return maxV, best_index

    pass
