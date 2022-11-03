from copy import deepcopy


class State(object):

    # Important:
    # grid = 64 bits
    # grid_8..0 = column_0
    # ...
    # grid_62..54 = column_6
    # bit_63 = unused
    # => column_i = 9 bits grid_9*i+8...9*i
    # column_i = [used_places = 3 bits, 6 flags]
    # flag_j = 0 if board_i_j is red (player 1) or 1 if board_i_j is yellow (player 2)
    def __init__(self):
        self.__grid: int = 0
        self.__played_moves: int = 0

    def __get_column_mask(self, column_number: int) -> int:
        return ((1 << (9 * (column_number + 1))) - 1) ^ ((1 << (9 * column_number)) - 1)

    def __get_column(self, column_number: int) -> int:
        return self.__grid & self.__get_column_mask(column_number)  # Needed 9 bits of column

    def __get_used_places(self, encoded_column: int):
        mask = (((1 << 9) - 1) ^ ((1 << 6) - 1))                    # mask = 111000000 in binary
        return (encoded_column & mask) >> 6

    def __set_column(self, encoded_column, column_number):
        inv_mask = ((1 << 64) - 1) ^ self.__get_column_mask(column_number)
        self.__grid &= inv_mask                                     # Clear the column
        self.__grid |= encoded_column << (9 * column_number)        # Set the updated column

    def __increment_used_places(self, column_number):
        encoded_column = self.__get_column(column_number)
        used_places = self.__get_used_places(encoded_column)
        used_places += 1

        pw2 = 2  # This is only the exponent (0, 1, 2), not 2^pw (1, 2, 4)
        while used_places > 0:
            if used_places >= (1 << pw2):
                # the added 6 because the used_places are bits (8,7,6) in each column
                encoded_column |= (1 << (6 + pw2))                      # Set the bit
                used_places -= (1 << pw2)
            else:
                encoded_column &= ((1 << 9) - 1) ^ (1 << (6 + pw2))     # Clear the bit

            pw2 -= 1

        self.__set_column(encoded_column, column_number)

    def __decode_column(self, encoded_column: int) -> list:
        decoded_column = []
        used_places = self.__get_used_places(encoded_column)
        for i in range(6):
            if i + 1 > used_places:
                decoded_column.append(0)
            else:
                bit = encoded_column & (1 << i)
                if bit == 0:
                    decoded_column.append(1)
                else:
                    decoded_column.append(2)
        return decoded_column

    def __can_play(self, column_number: int) -> bool:
        encoded_column = self.__get_column(column_number)
        used_places = self.__get_used_places(encoded_column)
        return used_places < 6

    # Important:
    # Board = int[6][7]
    # Board_i_j = 0 if it is uncolored
    # Board_i_j = 1 if it is played by first player (red)
    # Board_i_j = 2 if it is played by second player (yellow)
    def get_board(self) -> list:
        board = [[0 for i in range(7)] for j in range(6)]  # Initialize a 6x7 board
        for i in range(7):
            encoded_column = self.__get_column(i)
            decoded_column = self.__decode_column(encoded_column)
            for j in range(6):
                board[j][i] = decoded_column[j]
        return board

    def get_successor(self) -> list:
        successors = []
        for i in range(7):
            if self.__can_play(i):
                successor = deepcopy(self)
                successor.add_chip(i)
                successors.append(successor)
        return successors

    def add_chip(self, column_number: int):
        turn = self.__played_moves & 1  # turn = 0 for player 1 (red) and turn = 1 for player 2 (yellow)
        encoded_column = self.__get_column(column_number)
        used_places = self.__get_used_places(encoded_column)
        encoded_column |= turn * (1 << used_places)     # if used_places = x, we should sit bit number x
        self.__set_column(encoded_column, column_number)
        self.__increment_used_places(column_number)
        self.__played_moves += 1
