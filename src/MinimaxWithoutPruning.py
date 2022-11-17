import math

from . import Minimax
from . import Heuristic
from .Tree import Node


class MinimaxWithoutPruning(Minimax):
    def __init__(self, heuristic):
        self.__heuristic: Heuristic = heuristic

    def _Minimax__min_function(self, state, maxDepth):
        root = Node(self.__heuristic.get_score(state))
        result = self.__min_function_util(state, maxDepth, root)
        best_index = self.best_index(root.get_successor())
        return result, best_index, root

    def _Minimax__max_function(self, state, maxDepth):
        root=Node(self.__heuristic.get_score(state))
        result = self.__max_function_util(state, maxDepth, root)
        best_index = self.best_index(root.get_successor())
        return result, best_index, root

    def __min_function_util(self, state, maxDepth,root):
        if maxDepth <= 0:
            return self.__heuristic.get_score(state)

        states = state.get_successor()
        if len(states) == 0:
            return self.__heuristic.get_score(state)
        root.value = math.inf
        # i = 0
        for curr_state in states:
            child = Node(-1)
            root.add_successor(child)
            child.value = self.__max_function_util(curr_state, maxDepth - 1, child)
            # if v < minV:
            #     minV = v
            #     best_index = i
            # i += 1
            root.value = min(root.value, child.value)

        return root.value

    def __max_function_util(self, state, maxDepth, root):
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
            child.value = self.__min_function_util(curr_state, maxDepth - 1, child)
            # if v > maxV:
            #     maxV = v
            #     best_index = i
            # i += 1
            root.value= max(root.value, child.value)

        return root.value
