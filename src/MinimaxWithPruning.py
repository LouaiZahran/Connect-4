import math

from . import Minimax
from . import Heuristic


class MinimaxWithPruning(Minimax):
    def __init__(self,heuristic):
       self.__heuristic : Heuristic = heuristic

    def __min_function(self, state, maxDepth):
        self.__min_function_alpha_beta(state,-math.inf,math.inf,maxDepth)

    def __max_function(self,state,maxDepth):
        self.__max_function_alpha_beta(state,-math.inf,math.inf,maxDepth)
    def __min_function_alpha_beta(self,state,alpha,beta,maxDepth) :
        if maxDepth<=0 :
            return self.__heuristic.get_score(state)

        states=state.get_successor()
        if len(states)==0 :
            return self.__heuristic.get_score(state)
        minV = math.inf
        for curr_state in states:
            v=self.__max_function_alpha_beta(curr_state,alpha,beta,maxDepth-1)
            minV = min (minV, v)
            beta =min(beta,minV)
            if(beta<=alpha):
                return minV

        return minV

    def __max_function_alpha_beta(self, state,alpha,beta, maxDepth):
        if maxDepth<=0 :
            return self.__heuristic.get_score(state)

        states=state.get_successor()
        if len(states)==0 :
            return self.__heuristic.get_score(state)
        maxV=-math.inf
        for curr_state in states:
            v = self.__min_function_alpha_beta(curr_state,alpha,beta,maxDepth-1)
            maxV = max(maxV, v)
            alpha =max(alpha,maxV)
            if (beta <= alpha):
                return maxV

        return maxV


    pass
