import math

from . import Minimax
from . import Heuristic


class MinimaxWithPruning(Minimax):
    def __init__(self, heuristic):
        self.__heuristic: Heuristic = heuristic

    def __min_function(self, state, maxDepth):
        root=Tree(self.__heuristic.get_score(state))
        return self.__min_function_alpha_beta_util(state, -1, -math.inf, math.inf, maxDepth,root)

    def __max_function(self, state, maxDepth):
        root=Tree(self.__heuristic.get_score(state))
        return self.__max_function_alpha_beta_util(state, -1, -math.inf, math.inf, maxDepth,root)

    def __min_function_alpha_beta_util(self, state, best_index, alpha, beta, maxDepth):
        if maxDepth <= 0:
            return self.__heuristic.get_score(state), best_index,root

        states = state.get_successor()
        if len(states) == 0:
            return self.__heuristic.get_score(state), best_index,root
        minV = math.inf
        i = 0
        for curr_state in states:
            v,i,root = self.__max_function_alpha_beta_util(curr_state, best_index, alpha, beta, maxDepth - 1)
            root.add_child(v)
            if v < minV:
                minV = v
                best_index = i
            beta = min(beta, minV)
            if (beta <= alpha):
                return minV, best_index,root

        return minV, best_index,root

    def __max_function_alpha_beta_util(self, state, best_index, alpha, beta, maxDepth):
        if maxDepth <= 0:
            return self.__heuristic.get_score(state), best_index,root

        states = state.get_successor()
        if len(states) == 0:
            return self.__heuristic.get_score(state), best_index,root
        maxV = -math.inf
        i = 0
        for curr_state in states:
            v,i,root = self.__min_function_alpha_beta_util(curr_state, best_index, alpha, beta, maxDepth - 1)
            root.add_child(v)
            if maxV > v:
                maxV = v
                best_index = i
            i += 1
            alpha = max(alpha, maxV)
            if (beta <= alpha):
                return maxV, best_index,root

        return maxV, best_index,root