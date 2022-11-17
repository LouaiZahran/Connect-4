import math

from . import Minimax
from . import Heuristic
from .Tree import Node


class MinimaxWithPruning(Minimax):
    def __init__(self, heuristic):
        self.__heuristic: Heuristic = heuristic

    def _Minimax__min_function(self, state, maxDepth):
        root = Node(self.__heuristic.get_score(state))
        result = self.__min_function_alpha_beta_util(state, -math.inf, math.inf, maxDepth, root)
        best_index = self.best_index(root.get_successor())
        return result, best_index, root
    def _Minimax__max_function(self, state, maxDepth):
        root = Node(self.__heuristic.get_score(state))
        result = self.__max_function_alpha_beta_util(state, -math.inf, math.inf, maxDepth, root)
        best_index = self.best_index(root.get_successor())
        return result, best_index, root
    def __min_function_alpha_beta_util(self, state, alpha, beta, maxDepth, root):
        if maxDepth <= 0:
            return self.__heuristic.get_score(state)

        states = state.get_successor()
        if len(states) == 0:
            return self.__heuristic.get_score(state)
        root.value = math.inf
        i = 0
        for curr_state in states:
            child = Node(-1)
            root.add_successor(child)
            child.value = self.__max_function_alpha_beta_util(curr_state, alpha, beta, maxDepth - 1, child)
            # if v < minV:
            #     minV = v
            #     best_index = i
            root.value = min(root.value, child.value)
            beta = min(beta, child.value)
            if beta <= alpha:
                return root.value

        return root.value

    def __max_function_alpha_beta_util(self, state, alpha, beta, maxDepth, root):
        if maxDepth <= 0:
            return self.__heuristic.get_score(state)

        states = state.get_successor()
        if len(states) == 0:
            return self.__heuristic.get_score(state)
        root.value = -math.inf
        # i = 0
        for curr_state in states:
            child = Node(-1)
            root.add_successor(child)
            child.value = self.__min_function_alpha_beta_util(curr_state, alpha, beta, maxDepth - 1, child)
            # if v > maxV:
            #     maxV = v
            #     best_index = i
            # i += 1
            root.value = max(root.value, child.value)
            alpha = max(alpha, child.value)
            if beta <= alpha:
                return root.value

        return root.value
