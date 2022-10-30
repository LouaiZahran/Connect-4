
class State(object):
    def __init__(self):
        self.grid = None

    def get_successor(self):
        raise NotImplementedError
