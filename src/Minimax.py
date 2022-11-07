from . import State
import abc


class Minimax(object):

    def get_best_move(self, current_state: State, depth: int) -> int:
        best_index=self.__max_function(current_state,depth) [1]
        
        return best_index

    @abc.abstractmethod
    def __min_function(self, state, maxDepth): pass

    @abc.abstractmethod
    def __max_function(self,state,maxDepth): pass
