import sys
from copy import deepcopy

import pygame


class GUI(object):
    __WIDTH = 639
    __HEIGHT = 553
    __CIRCLE_SIZE = 59
    __SPACE_SIZE = 28
    __CHIP_SPEED = 10

    def __init__(self):
        pygame.init()
        icon = pygame.image.load("../assets/icon.png")
        pygame.display.set_icon(icon)
        pygame.display.set_caption("Connect Four")
        self.screen = pygame.display.set_mode((GUI.__WIDTH, GUI.__HEIGHT))
        self.screen.fill((255, 255, 255))

        self.board_surface = pygame.image.load("../assets/Connect4_Board_transparent.png")
        self.red_chip_surface = pygame.image.load("../assets/ChipRed.png")
        self.yellow_chip_surface = pygame.image.load("../assets/ChipYellow.png")

        self.red_chip_surface = pygame.transform.scale(self.red_chip_surface, (60, 60))
        self.yellow_chip_surface = pygame.transform.scale(self.yellow_chip_surface, (60, 60))
        # self.board_surface = pygame.transform.scale(self.board_surface, (GUI.__WIDTH, GUI.__HEIGHT))

        self.labels_font = pygame.font.SysFont("arial", 20)
        self.player_score_label = self.labels_font.render("Player score: ", True, (0, 0, 0))
        self.ai_score_label = self.labels_font.render("AI score: ", True, (0, 0, 0))

        self.screen.blit(self.board_surface, (0, 0))

        self.columns = []
        for i in range(7):
            self.columns.append(pygame.Rect((i * (GUI.__SPACE_SIZE + GUI.__CIRCLE_SIZE), 0),
                                            (GUI.__SPACE_SIZE + GUI.__CIRCLE_SIZE, GUI.__HEIGHT)))

        pygame.display.update()

    def add_chip(self, column_number, turn, below, animate, player_score, ai_score):
        surface = self.red_chip_surface if turn & 1 == 1 else self.yellow_chip_surface

        if animate:
            previous_screen = self.screen.copy()
            current_y = -GUI.__CIRCLE_SIZE
            while current_y < GUI.__HEIGHT - (below[column_number] + 1) * (GUI.__SPACE_SIZE + GUI.__CIRCLE_SIZE):
                self.screen.blit(previous_screen, (0, 0))
                self.screen.blit(surface,
                                 (column_number * (GUI.__SPACE_SIZE + GUI.__CIRCLE_SIZE) + GUI.__SPACE_SIZE,
                                  current_y))
                self.display_score(player_score, ai_score)
                pygame.display.update()
                current_y += GUI.__CHIP_SPEED
            self.screen.blit(previous_screen, (0, 0))

        self.screen.blit(surface,
                         (column_number * (GUI.__SPACE_SIZE + GUI.__CIRCLE_SIZE) + GUI.__SPACE_SIZE,
                          GUI.__HEIGHT - (below[column_number] + 1) * (GUI.__SPACE_SIZE + GUI.__CIRCLE_SIZE)))
        self.screen.blit(self.board_surface, (0, 0))

        pygame.display.update()

        below[column_number] += 1

    def display_grid(self, board, added_chip_column, animate, player_score, ai_score):
        below = [0 for i in range(7)]
        for row in range(6):
            for col in range(7):
                if board[row][col] != 0:
                    self.add_chip(col, board[row][col], below, animate and col == added_chip_column and (row == 5 or board[row + 1][col] == 0), player_score, ai_score)
        self.display_score(player_score, ai_score)
        pygame.display.update()

    def display_score(self, player_score, ai_score):
        self.player_score_label = self.labels_font.render("Player Score: " + str(player_score), True, (0, 0, 0))
        self.ai_score_label = self.labels_font.render("AI Score: " + str(ai_score), True, (0, 0, 0))

        # Erase previous score
        self.screen.blit(self.board_surface, (0, 0))

        # Render new score
        self.screen.blit(self.player_score_label, (30, 8))
        self.screen.blit(self.ai_score_label, (500, 8))

    def take_input(self):
        while True:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    sys.exit(0)

                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = event.pos
                    for i in range(7):
                        if self.columns[i].collidepoint(x, y):
                            return i