import math
from . import Heuristic
from . import State


class Heuristic1(Heuristic):
    __max_value = math.pow(10, 12)

    def get_score(self, current_state: State):
        board: list = current_state.get_board()
        return self.__get_score_of_rows(board) + \
               self.__get_score_of_columns(board) + \
               self.__get_score_of_diagonals(board)

    def __get_score_of_rows(self, board: list):
        result: int = 0
        for i in range(6):
            j = 0
            empty_before = 0
            while j < 7:
                while j < 7 and board[i][j] == 0:
                    empty_before += 1
                    j += 1
                if empty_before == 7:
                    break
                if j < 7:
                    first_group = 0
                    player = board[i][j]
                    player_j = j
                    while j < 7 and board[i][j] == player:
                        first_group += 1
                        j += 1
                    if j == 7 or (j < 7 and board[i][j] != 0):  # if the opponent is in my road, stop
                        result += self.__calc_group(player, player_j, empty_before, first_group, 0, 0)
                        continue  # start new grouping
                    empty_between = 0
                    while j < 7 and board[i][j] == 0:
                        empty_between += 1
                        j += 1
                    if empty_between > 1 or j == 7 or (j < 7 and board[i][j] ^ player == 3):  # check
                        result += self.__calc_group(player, player_j, empty_before, first_group, empty_between, 0)
                        empty_before = empty_between
                        continue
                    second_group = 0
                    while j < 7 and board[i][j] == player:
                        second_group += 1
                        j += 1
                    if first_group == 1 and second_group == 1:
                        result += self.__sum_result(player, self.__calc_single_chip(j, empty_before + empty_between))
                        j -= 1
                        empty_before = empty_between
                        continue
                    else:
                        result += self.__calc_group(player, player_j, empty_before,
                                                    first_group, empty_between, second_group)
        return result

    def __get_score_of_columns(self, board: list):
        result: int = 0
        for j in range(7):
            i = 0
            while i < 6:
                if board[i][j] == 0:
                    break
                first_group = 0
                player = board[i][j]
                while i < 6 and board[i][j] == player:
                    first_group += 1
                    i += 1
                if i < 6 and board[i][j] == 0:
                    result += self.__calc_group(player, j, 0, first_group, 6 - i, 0)
                else:
                    result += self.__calc_group(player, j, 0, first_group, 0, 0)
        return result

    def __get_score_of_diagonals(self, board):
        return self.__get_score_of_main_diagonals_lower(board) + self.__get_score_of_main_diagonals_upper(board) + \
               self.__get_score_of_anti_diagonals_lower(board) + self.__get_score_of_anti_diagonals_upper(board)

    def __get_score_of_anti_diagonals_lower(self, board: list):
        result: int = 0
        for k in range(1, 4):
            i, j = 0, k
            empty_before = 0
            while j < 7:
                while j < 7 and board[i][j] == 0:
                    empty_before += 1
                    i += 1
                    j += 1
                if empty_before + k == 7:
                    break
                if j < 7:
                    first_group = 0
                    player = board[i][j]
                    player_j = j
                    while j < 7 and board[i][j] == player:
                        first_group += 1
                        i += 1
                        j += 1
                    if j == 7 or (j < 7 and board[i][j] != 0):  # if the opponent is in my road, stop
                        result += self.__calc_group(player, player_j, empty_before, first_group, 0, 0)
                        continue  # start new grouping
                    empty_between = 0
                    while j < 7 and board[i][j] == 0:
                        empty_between += 1
                        i += 1
                        j += 1
                    if empty_between > 1 or j == 7 or (j < 7 and board[i][j] ^ player == 3):  # check
                        result += self.__calc_group(player, player_j, empty_before, first_group, empty_between,
                                                            0)
                        empty_before = empty_between
                        continue
                    second_group = 0
                    while j < 7 and board[i][j] == player:
                        second_group += 1
                        i += 1
                        j += 1
                    if first_group == 1 and second_group == 1:
                        result += self.__sum_result(player, self.__calc_single_chip(j, empty_before + empty_between))
                        i -= 1
                        j -= 1
                        empty_before = empty_between
                        continue
                    else:
                        result += self.__calc_group(player, player_j, empty_before,
                                                    first_group, empty_between, second_group)
        return result

    def __get_score_of_anti_diagonals_upper(self, board: list):
        result: int = 0
        for k in range(3):
            i, j = k, 0
            empty_before = 0
            while i < 6:
                while i < 6 and board[i][j] == 0:
                    empty_before += 1
                    i += 1
                    j += 1
                if empty_before + k == 6:
                    break
                if i < 6:
                    first_group = 0
                    player = board[i][j]
                    player_j = j
                    while i < 6 and board[i][j] == player:
                        first_group += 1
                        i += 1
                        j += 1
                    if i == 6 or (i < 6 and board[i][j] != 0):  # if the opponent is in my road, stop
                        result += self.__calc_group(player, player_j, empty_before, first_group, 0, 0)
                        continue  # start new grouping
                    empty_between = 0
                    while i < 6 and board[i][j] == 0:
                        empty_between += 1
                        i += 1
                        j += 1
                    if empty_between > 1 or i == 6 or (i < 6 and board[i][j] ^ player == 3):  # check
                        result += self.__calc_group(player, player_j, empty_before, first_group, empty_between, 0)
                        empty_before = empty_between
                        continue
                    second_group = 0
                    while i < 6 and board[i][j] == player:
                        second_group += 1
                        i += 1
                        j += 1
                    if first_group == 1 and second_group == 1:
                        result += self.__sum_result(player, self.__calc_single_chip(j, empty_before + empty_between))
                        i -= 1
                        j -= 1
                        empty_before = empty_between
                        continue
                    else:
                        result += self.__calc_group(player, player_j, empty_before, first_group, empty_between,
                                                    second_group)
        return result

    def __get_score_of_main_diagonals_lower(self, board: list):
        result: int = 0
        for k in range(3, 6):
            i, j = k, 0
            empty_before = 0
            while i >= 0:
                while i >= 0 and board[i][j] == 0:
                    empty_before += 1
                    i -= 1
                    j += 1
                if empty_before - k == 1:
                    break
                if i >= 0:
                    first_group = 0
                    player = board[i][j]
                    player_j = j
                    while i >= 0 and board[i][j] == player:
                        first_group += 1
                        i -= 1
                        j += 1
                    if i == 0 or (i >= 0 and board[i][j] != 0):  # if the opponent is in my road, stop
                        result += self.__calc_group(player, player_j, empty_before, first_group, 0, 0)
                        continue  # start new grouping
                    empty_between = 0
                    while i >= 0 and board[i][j] == 0:
                        empty_between += 1
                        i -= 1
                        j += 1
                    if empty_between > 1 or i == 0 or (i >= 0 and board[i][j] ^ player == 3):  # check
                        result += self.__calc_group(player, player_j, empty_before, first_group, empty_between, 0)
                        empty_before = empty_between
                        continue
                    second_group = 0
                    while i >= 0 and board[i][j] == player:
                        second_group += 1
                        i -= 1
                        j += 1
                    if first_group == 1 and second_group == 1:
                        result += self.__sum_result(player, self.__calc_single_chip(j, empty_before + empty_between))
                        i += 1
                        j -= 1
                        empty_before = empty_between
                        continue
                    else:
                        result += self.__calc_group(player, player_j, empty_before,
                                                    first_group, empty_between, second_group)
        return result

    def __get_score_of_main_diagonals_upper(self, board: list):
        result: int = 0
        for k in range(1, 4):
            i, j = 5, k
            empty_before = 0
            while j < 7:
                while j < 7 and board[i][j] == 0:
                    empty_before += 1
                    i -= 1
                    j += 1
                if empty_before + k == 7:
                    break
                if j < 7:
                    first_group = 0
                    player = board[i][j]
                    player_j = j
                    while j < 7 and board[i][j] == player:
                        first_group += 1
                        i -= 1
                        j += 1
                    if j == 7 or (j < 7 and board[i][j] != 0):  # if the opponent is in my road, stop
                        result += self.__calc_group(player, player_j, empty_before, first_group, 0, 0)
                        continue  # start new grouping
                    empty_between = 0
                    while j < 7 and board[i][j] == 0:
                        empty_between += 1
                        i -= 1
                        j += 1
                    if empty_between > 1 or j == 7 or (j < 7 and board[i][j] ^ player == 3):  # check
                        result += self.__calc_group(player, player_j, empty_before, first_group, empty_between, 0)
                        empty_before = empty_between
                        continue
                    second_group = 0
                    while j < 7 and board[i][j] == player:
                        second_group += 1
                        i -= 1
                        j += 1
                    if first_group == 1 and second_group == 1:
                        result += self.__sum_result(player, self.__calc_single_chip(j, empty_before + empty_between))
                        i += 1
                        j -= 1
                        empty_before = empty_between
                        continue
                    else:
                        result += self.__calc_group(player, player_j, empty_before,
                                                    first_group, empty_between, second_group)
        return result

    def __calc_group(self, player, j, empty_before, first_group, empty_between, second_group):
        result: int = 0
        empty_spaces = empty_before + empty_between
        if first_group == 1 and second_group == 0:  # single chip
            result += self.__calc_single_chip(j, empty_spaces)
        elif first_group == 2 and second_group == 0:  # Two chips
            result += self.__calc_two_chips(empty_spaces)
        elif first_group + second_group == 3:  # Three chips
            result += self.__calc_three_chips(empty_before, first_group, empty_between, second_group)
        else:  # Four or more chips
            result += self.__calc_more_than_three_chips(empty_before, first_group, empty_between, second_group)
        return self.__sum_result(player, result)

    def __calc_single_chip(self, j: int, empty_spaces) -> int:
        if empty_spaces < 3:
            return 0
        if j == 0 or j == 6:
            result = 40
        elif j == 1 or j == 5:
            result = 70
        elif j == 2 or j == 4:
            result = 120
        else:
            result = 200
        return result

    def __calc_two_chips(self, empty_spaces: int):
        if empty_spaces < 2:
            return 0
        return (empty_spaces - 1) * 10000

    def __calc_three_chips(self, empty_before, first_group, empty_between, second_group):
        result: int = 0
        empty_spaces = empty_before + empty_between
        if first_group + second_group + empty_spaces < 4:
            return 0
        if first_group == 3 and empty_before >= 1 and empty_between >= 1:  # unstoppable case
            result += self.__max_value
        else:
            result += 900000
        return result

    def __calc_more_than_three_chips(self, empty_before, first_group, empty_between, second_group):
        result: int = 0
        if first_group >= 4 and empty_before >= 1 and empty_between >= 1:  # unstoppable case
            result += (first_group - 2) * self.__max_value
        elif first_group >= 4:
            result += (first_group - 3) * self.__max_value
        if second_group >= 4:
            result += (second_group - 3) * self.__max_value
        if empty_between == 1:
            temp = first_group + second_group - 2
            if first_group >= 4:
                temp -= (first_group - 3)
            if second_group >= 4:
                temp -= (second_group - 3)
            if temp > 0:
                result += temp * 900000
        return result

    def __sum_result(self, player, result):
        if player == 1:
            return -result
        return result
