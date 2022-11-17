from src import State


class final_score(object):

    def get_final_score(self, state: State):
        board = state.get_board()
        return self.__get_score_of_rows(board) + self.__get_score_of_columns(board) + self.__get_score_of_diagonals(board)

    def __get_score_of_rows(self, board):
        result: int = 0
        for i in range(6):
            j = 0
            while j < 4:
                player = board[i][j]
                if player == 0:
                    j += 1
                    continue
                count = 0
                while j < 7 and player == board[i][j]:
                    count += 1
                    j += 1
                result += self.__sum_result(player, count)
        return result

    def __get_score_of_columns(self, board):
        result: int = 0
        for j in range(7):
            i = 0
            while i < 3:
                player = board[i][j]
                if player == 0:
                    break
                count = 0
                while i < 6 and player == board[i][j]:
                    count += 1
                    i += 1
                result += self.__sum_result(player, count)
        return result

    def __get_score_of_diagonals(self, board):
        return self.__get_score_of_anti_diagonal_lower(board) + self.__get_score_of_anti_diagonal_upper(board) +\
               self.__get_score_of_main_diagonal_lower(board) + self.__get_score_of_main_diagonal_upper(board)

    def __get_score_of_anti_diagonal_lower(self, board):
        result: int = 0
        for k in range(1, 4):
            i, j = 0, k
            while j < 4:
                player = board[i][j]
                if player == 0:
                    i += 1
                    j += 1
                    continue
                count = 0
                while j < 7 and player == board[i][j]:
                    count += 1
                    j += 1
                    i += 1
                result += self.__sum_result(player, count)
        return result

    def __get_score_of_anti_diagonal_upper(self, board):
        result: int = 0
        for k in range(3):
            i, j = k, 0
            while i < 3:
                player = board[i][j]
                if player == 0:
                    i += 1
                    j += 1
                    continue
                count = 0
                while i < 6 and player == board[i][j]:
                    count += 1
                    j += 1
                    i += 1
                result += self.__sum_result(player, count)
        return result

    def __get_score_of_main_diagonal_lower(self, board):
        result: int = 0
        for k in range(3, 6):
            i, j = k, 0
            while i > 2:
                player = board[i][j]
                if player == 0:
                    i -= 1
                    j += 1
                    continue
                count = 0
                while i >= 0 and player == board[i][j]:
                    count += 1
                    j += 1
                    i -= 1
                result += self.__sum_result(player, count)
        return result

    def __get_score_of_main_diagonal_upper(self, board):
        result: int = 0
        for k in range(1, 4):
            i, j = 5, k
            while j < 4:
                player = board[i][j]
                if player == 0:
                    i -= 1
                    j += 1
                    continue
                count = 0
                while j < 7 and player == board[i][j]:
                    count += 1
                    j += 1
                    i -= 1
                result += self.__sum_result(player, count)
        return result

    def __sum_result(self, player, count):
        if count < 4:
            return 0
        count -= 3
        if player == 1:
            return -count
        return count
