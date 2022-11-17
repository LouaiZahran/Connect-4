import math

from . import Minimax
from . import Heuristic
from .Tree import Node


class MinimaxWithPruning(Minimax):
    def __init__(self, heuristic):
        self.__heuristic: Heuristic = heuristic

    def _Minimax__min_function(self, state, maxDepth):
        root = Node(self.__heuristic.get_score(state))
        return self.__min_function_alpha_beta_util(state, -1, -math.inf, math.inf, maxDepth, root), root

    def _Minimax__max_function(self, state, maxDepth):
        root = Node(self.__heuristic.get_score(state))
        return self.__max_function_alpha_beta_util(state, -1, -math.inf, math.inf, maxDepth, root), root

    def __min_function_alpha_beta_util(self, state, best_index, alpha, beta, maxDepth, root):
        if maxDepth <= 0:
            return self.__heuristic.get_score(state), best_index

        states = state.get_successor()
        if len(states) == 0:
            return self.__heuristic.get_score(state), best_index
        minV = math.inf
        i = 0
        for curr_state in states:
            child = Node(-1)
            root.add_successor(child)
            v, i = self.__max_function_alpha_beta_util(curr_state, best_index, alpha, beta, maxDepth - 1)
            child.value=v
            if v < minV:
                minV = v
                best_index = i
            beta = min(beta, minV)
            root.value=minV
            if (beta <= alpha):
                return minV, best_index

        return minV, best_index

    def __max_function_alpha_beta_util(self, state, best_index, alpha, beta, maxDepth, root):
        if maxDepth <= 0:
            return self.__heuristic.get_score(state), best_index

        states = state.get_successor()
        if len(states) == 0:
            return self.__heuristic.get_score(state), best_index
        maxV = -math.inf
        i = 0
        for curr_state in states:
            child = Node(-1)
            root.add_successor(child)
            v, i = self.__min_function_alpha_beta_util(curr_state, best_index, alpha, beta, maxDepth - 1)
            child.value=v
            if v > maxV:
                maxV = v
                best_index = i
            i += 1
            alpha = max(alpha, maxV)
            root.value=maxV
            if beta <= alpha:
                return maxV, best_index

        return maxV, best_index
