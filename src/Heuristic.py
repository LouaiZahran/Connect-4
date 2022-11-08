from . import State
import abc


class Heuristic(object):
    @abc.abstractmethod
    def get_score(self, current_state: State):
        pass
