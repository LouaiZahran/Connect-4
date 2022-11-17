from src import State


class final_score(object):

    def get_final_score(self, state: State):
        board = state.get_board()
        user_score = self.__get_score_of_rows(board, 1) + self.__get_score_of_columns(board, 1) +\
                     self.__get_score_of_diagonals(board, 1)
        agent_score = self.__get_score_of_rows(board, 2) + self.__get_score_of_columns(board, 2) + \
                     self.__get_score_of_diagonals(board, 2)
        return user_score, agent_score

    def __get_score_of_rows(self, board, player: int):
        result: int = 0
        for i in range(6):
            j = 0
            while j < 4:
                if board[i][j] != player:
                    j += 1
                    continue
                count = 0
                while j < 7 and player == board[i][j]:
                    count += 1
                    j += 1
                result += self.__sum_result(count)
        return result

    def __get_score_of_columns(self, board, player: int):
        result: int = 0
        for j in range(7):
            i = 0
            while i < 3:
                if board[i][j] == 0:
                    break
                if board[i][j] ^ player == 3:
                    i += 1
                    continue
                count = 0
                while i < 6 and player == board[i][j]:
                    count += 1
                    i += 1
                result += self.__sum_result(count)
        return result

    def __get_score_of_diagonals(self, board, player: int):
        return self.__get_score_of_anti_diagonal_lower(board, player) +\
               self.__get_score_of_anti_diagonal_upper(board, player) +\
               self.__get_score_of_main_diagonal_lower(board, player) +\
               self.__get_score_of_main_diagonal_upper(board, player)

    def __get_score_of_anti_diagonal_lower(self, board, player: int):
        result: int = 0
        for k in range(1, 4):
            i, j = 0, k
            while j < 4:
                if board[i][j] != player:
                    i += 1
                    j += 1
                    continue
                count = 0
                while j < 7 and player == board[i][j]:
                    count += 1
                    j += 1
                    i += 1
                result += self.__sum_result(count)
        return result

    def __get_score_of_anti_diagonal_upper(self, board, player: int):
        result: int = 0
        for k in range(3):
            i, j = k, 0
            while i < 3:
                if board[i][j] != player:
                    i += 1
                    j += 1
                    continue
                count = 0
                while i < 6 and player == board[i][j]:
                    count += 1
                    j += 1
                    i += 1
                result += self.__sum_result(count)
        return result

    def __get_score_of_main_diagonal_lower(self, board, player: int):
        result: int = 0
        for k in range(3, 6):
            i, j = k, 0
            while i > 2:
                if board[i][j] != player:
                    i -= 1
                    j += 1
                    continue
                count = 0
                while i >= 0 and player == board[i][j]:
                    count += 1
                    j += 1
                    i -= 1
                result += self.__sum_result(count)
        return result

    def __get_score_of_main_diagonal_upper(self, board, player: int):
        result: int = 0
        for k in range(1, 4):
            i, j = 5, k
            while j < 4:
                if board[i][j] != player:
                    i -= 1
                    j += 1
                    continue
                count = 0
                while j < 7 and player == board[i][j]:
                    count += 1
                    j += 1
                    i -= 1
                result += self.__sum_result(count)
        return result

    def __sum_result(self, count):
        if count < 4:
            return 0
        return count - 3
