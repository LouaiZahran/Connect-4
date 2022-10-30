
class Controller(object):
    def __init__(self):
        self.current_state = None
        self.current_turn = False

    def get_options(self):
        raise NotImplementedError

    def play_turn(self):
        raise NotImplementedError

    def get_user_move(self):
        raise NotImplementedError

    def get_agent_move(self):
        raise NotImplementedError

    def start(self):
        raise NotImplementedError


if __name__ == "__main__":
    controller = Controller()
    controller.start()
