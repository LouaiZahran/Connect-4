import math

from . import Minimax
from . import Heuristic


class MinimaxWithoutPruning(Minimax):

    def __init__(self,heuristic):
       self.__heuristic : Heuristic = heuristic

    def __min_function(self,state,maxDepth) :
        if maxDepth<=0 :
            return self.__heuristic.get_score(state)

        states=state.get_successor()
        if len(states)==0 :
            return self.__heuristic.get_score(state)
        minV=math.inf
        for curr_state in states:
            v=self.__max_function(curr_state,maxDepth-1)
            minV = min(minV, v)

        return minV

    def __max_function(self,state,maxDepth):
        if maxDepth<=0 :
            return self.__heuristic.get_score(state)

        states=state.get_successor()
        if len(states)==0 :
            return self.__heuristic.get_score(state)
        maxV=-math.inf
        for curr_state in states:
            v = self.__min_function(curr_state,maxDepth-1)
            maxV = min(maxV, v)

        return maxV




    pass

