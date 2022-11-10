import math
from . import State, Heuristic


class Heuristic1(Heuristic):
    __max_value = math.pow(10, 12)

    def get_score(self, current_state: State):
        board = current_state.get_board()
        result: int = self.__get_single_chips(board) + self.__get_two_chips(board) + \
                      self.__get_three_chips(board) + self.__get_three_chips(board)
        return result

    def __get_single_chips(self, board: list) -> int:
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
                value = 24
            elif i == 1 or i == 4:
                value = 32
            else:
                value = 40
        elif j == 1 or j == 5:
            if i == 0 or i == 5:
                value = 35
            elif i == 1 or i == 4:
                value = 53
            else:
                value = 70
        elif j == 2 or j == 4:
            if i == 0 or i == 5:
                value = 55
            elif i == 1 or i == 4:
                value = 87
            else:
                value = 120
        else:
            if i == 0 or i == 5:
                value = 108
            elif i == 1 or i == 4:
                value = 154
            else:
                value = 200
        if player == 1:
            return -value
        return value

    def __get_two_chips(self, board: list) -> int:
        result: int = 0
        for i in range(6):
            for j in range(6):
                if board[i][j] == 0:
                    continue
                if board[i][j] == board[i][j + 1]:
                    empty_spaces = 0
                    k = j - 1
                    while k >= 0 and board[i][k] == 0:
                        empty_spaces += 1
                        k -= 1
                    k = j + 2
                    while k < 7 and board[i][k] == 0:
                        empty_spaces += 1
                        k += 1
                    result += self.__calc_two_chips(board[i][j], empty_spaces)
        for j in range(7):
            for i in range(3):
                if board[i][j] == 0:
                    break
                if board[i][j] == board[i + 1][j]:
                    empty_spaces = 0
                    for k in range(i + 2, 6):
                        if board[k][j] != 0:
                            break
                        empty_spaces += 1
                    result += self.__calc_two_chips(board[i][j], empty_spaces)
        for i in range(5):
            for j in range(6):
                if board[i][j] == 0:
                    break
                if board[i][j] == board[i + 1][j + 1]:
                    r, c = i - 1, j - 1
                    empty_spaces = 0
                    while r >= 0 and c >= 0 and board[r][c] == 0:
                        empty_spaces += 1
                        r -= 1
                        c -= 1
                    r, c = i + 2, j + 2
                    while r < 6 and c < 7 and board[r][c] == 0:
                        empty_spaces += 1
                        r += 1
                        c += 1

                    result += self.__calc_two_chips(board[i][j], empty_spaces)
            for j in range(6, 0, -1):
                if board[i][j] == 0:
                    break
                if board[i][j] == board[i + 1][j - 1]:
                    r, c = i - 1, j + 1
                    empty_spaces = 0
                    while r >= 0 and c < 6 and board[r][c] == 0:
                        empty_spaces += 1
                        r -= 1
                        c += 1
                    r, c = i + 2, j - 2
                    while r < 6 and c >= 0 and board[r][c] == 0:
                        empty_spaces += 1
                        r += 1
                        c -= 1
                    result += self.__calc_two_chips(board[i][j], empty_spaces)
        return result

    def __calc_two_chips(self, player: int, empty_spaces: int):
        result: int = 0
        if empty_spaces > 1:
            if player == 1:
                result -= (empty_spaces - 1) * 10000
            else:
                result += (empty_spaces - 1) * 10000
        return result

    def __get_three_chips(self):
        return 0  # to be implemented

    def __get_four_chips(self):
        return 0  # to be implemented
