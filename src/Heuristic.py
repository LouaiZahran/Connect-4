import abc
from . import State


class Heuristic(object):

    @abc.abstractmethod
    def get_score(self, current_state: State):
        pass
