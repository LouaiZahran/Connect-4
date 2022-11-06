from . import State
import abc


class Minimax(object):

    def get_best_move(self, current_state: State, depth: int) -> int:
        self.__max_function(current_state,depth)

        return 0

    @abc.abstractmethod
    def __min_function(self, state, maxDepth): pass

    @abc.abstractmethod
    def __max_function(self,state,maxDepth): pass
