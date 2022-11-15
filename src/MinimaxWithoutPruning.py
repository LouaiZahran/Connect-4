import math

from . import Minimax
from . import Heuristic
from . import Tree


class MinimaxWithoutPruning(Minimax):
    def __init__(self, heuristic):
        self.__heuristic: Heuristic = heuristic

    def __min_function(self, state, maxDepth):
        root=Tree(self.__heuristic.get_score(state))
        return self.__min_function_util(state, -1, maxDepth,root)

    def __max_function(self, state, maxDepth):
        root=Tree(self.__heuristic.get_score(state))
        return self.__max_function_util(state, -1, maxDepth,root)

    def __min_function_util(self, state, best_index, maxDepth,root):
        if maxDepth <= 0:
            return self.__heuristic.get_score(state), best_index,root

        states = state.get_successor()
        if len(states) == 0:
            return self.__heuristic.get_score(state), best_index ,root
        minV = math.inf
        i = 0
        for curr_state in states:
            v = self.__max_function_util(curr_state,best_index, maxDepth - 1,root)
            root.add_child(v)
            if v < minV:
                minV = v
                best_index = i
            i += 1

        return minV, best_index ,root

    def __max_function_util(self, state, best_index, maxDepth,root):
        if maxDepth <= 0:
            return self.__heuristic.get_score(state), best_index,root

        states = state.get_successor()
        if len(states) == 0:
            return self.__heuristic.get_score(state) , best_index,root
        maxV = -math.inf
        i = 0
        for curr_state in states:
            v = self.__min_function_util(curr_state,best_index, maxDepth - 1,root)
            root.add_child(v)
            if maxV > v:
                maxV = v
                best_index = i
            i += 1

        return maxV, best_index ,root,root

    pass
