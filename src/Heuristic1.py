import math
from . import Heuristic
from . import State


class Heuristic1(Heuristic):
    __max_value = math.pow(10, 12)

    def get_score(self, current_state: State):
        board = current_state.get_board()
        result: int = 0
        for i in range(6):
            j = 0
            while j < 7:
                empty_before = 0
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
                    if j < 7 and board[i][j] != 0:  # if the opponent is in my road, stop
                        result += self.__sum_result(player, self.__calc_group(player, player_j, empty_before,
                                                                              first_group, 0, 0))
                        break  # start new grouping
                    empty_between = 0
                    while j < 7 and board[i][j] == 0:
                        empty_between += 1
                        j += 1
                    if empty_between > 1 or (j < 7 and board[i][j] ^ player == 3):  # check
                        result += self.__sum_result(player, self.__calc_group(player, player_j, empty_before,
                                                                              first_group, empty_between, 0))
                        break
                    second_group = 0
                    while j < 7 and board[i][j] == player:
                        second_group += 1
                        j += 1
                    if first_group == 1 and second_group == 1:
                        result += self.__sum_result(player,
                                                    self.__calc_single_chip(player, j, empty_before + empty_between))
                        j -= 1
                        break
                    else:
                        result += self.__sum_result(player, self.__calc_group(player, player_j, empty_before,
                                                                              first_group, empty_between, second_group))
        return result

    def __calc_group(self, player, j, empty_before, first_group, empty_between, second_group):
        result: int = 0
        empty_spaces = empty_before + empty_between
        if first_group == 1 and second_group == 0:  # single chip
            result += self.__calc_single_chip(player, j, empty_spaces)
        elif first_group == 2 and second_group == 0:  # Two chips
            result += self.__calc_two_chips(player, empty_spaces)
        elif first_group <= 3 or second_group <= 3:  # Three chips
            result += self.__calc_three_chips(player, empty_before, first_group, empty_between, second_group)
        else:  # Four or more chips
            result += self.__calc_more_than_three_chips(player, empty_before, first_group, empty_between, second_group)
        return self.__sum_result(player, result)

    def __calc_single_chip(self, player: int, j: int, empty_spaces) -> int:
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

    def __calc_two_chips(self, player: int, empty_spaces: int):
        if empty_spaces < 2:
            return 0
        return (empty_spaces - 1) * 10000

    def __calc_three_chips(self, player, empty_before, first_group, empty_between, second_group):
        result: int = 0
        empty_spaces = empty_before + empty_between
        if first_group + second_group + empty_spaces <= 3:
            return 0
        if first_group == 3 and empty_before >= 1 and empty_between >= 1:  # unstoppable case
            result += self.__max_value
        elif empty_between == 1:
            result += 900000
        return result

    def __calc_more_than_three_chips(self, player, empty_before, first_group, empty_between, second_group):
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
