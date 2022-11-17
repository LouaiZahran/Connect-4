from . import Heuristic
from . import State


class Heuristic2(Heuristic):

    def __int__(self):
        pass


    def get_score(self, current_state: State):
        board = current_state.get_board()
        result: int = 0
        for j in range(7):
            for i in range(6):
                if board[i][j] == 0:
                    break
                result += self.__calc_single_chip(board[i][j], i, j)
        return result

    def __calc_single_chip(self, player: int, i: int, j: int) -> int:
        if j == 0 or j == 6:
            if i == 0 or i == 5:
                value = 3
            elif i == 1 or i == 4:
                value = 4
            else:
                value = 5
        elif j == 1 or j == 5:
            if i == 0 or i == 5:
                value = 4
            elif i == 1 or i == 4:
                value = 6
            else:
                value = 8
        elif j == 2 or j == 4:
            if i == 0 or i == 5:
                value = 5
            elif i == 1 or i == 4:
                value = 8
            else:
                value = 11
        else:
            if i == 0 or i == 5:
                value = 7
            elif i == 1 or i == 4:
                value = 10
            else:
                value = 13
        if player == 1:
            return -value
        return value
