import tic_tac_toe
import math
import random

_PROBABILITIES = { # [win, draw, lose]
    "hard": [1, 0, 0],
    "medium": [0.3, 0.5, 0.2],
    "easy": [0.1, 0.4, 0.5]
}

class Bot:
    def __init__(self, turn_status, difficulty="hard"):
        self.difficulty = difficulty
        self.turn_status = turn_status

        self.delay = 0.5
        self.bot_turn = False
        self.turn_delay = 0.3

    def choose(self, grid):
        outcome_data = self.evaluate(grid)

        outcomes = [self.turn_status, 0, -self.turn_status]

        base_probability = _PROBABILITIES[self.difficulty].copy()
        base_probability = _PROBABILITIES[self.difficulty]

        outcome_choices = []
        probabilities_list = []
        removed_sum = 0.0

        for i, p in enumerate(base_probability):
            outcome_list = outcome_data[outcomes[i]]
            if len(outcome_list) > 0:
                probabilities_list.append(p)
                outcome_choices.append(outcome_list)
            else:
                removed_sum += p

        if probabilities_list:
            probabilities_list[0] += removed_sum

        output = self.get_choice_from_probability(probabilities_list)
        choice_list = outcome_choices[output]
        return random.choice(choice_list)

    def evaluate(self, grid):
        unoccupied_tiles = []
        for i in range(len(grid)):
            for j in range(len(grid)):
                if grid[i][j] == 0:
                    unoccupied_tiles.append((i,j))

        if self.turn_status == 1:
            is_maximizing_player = True
        else:
            is_maximizing_player = False

        outcome_data = {
            -1: [],
            0: [],
            1: []
        }

        if len(unoccupied_tiles) == len(grid) ** 2:
            outcome_data[0] = unoccupied_tiles
        else:
            for tile in unoccupied_tiles:
                i,j = tile[0], tile[1]

                modified_grid = [x.copy() for x in grid]
                modified_grid[i][j] = -1

                modified_unoccupied = unoccupied_tiles.copy()
                modified_unoccupied.remove(tile)

                tile_outcome = self.minimax(modified_grid, modified_unoccupied, not is_maximizing_player)
                outcome_data[tile_outcome].append((i,j))

        return outcome_data

    @staticmethod
    def minimax(grid, unoccupied_tiles, maximizing_player):
        _, game_state = tic_tac_toe.TicTacToe.check_game(grid)
        if len(unoccupied_tiles) == 0 or game_state != 0:
            return game_state

        if maximizing_player:
            max_evaluation = -math.inf
            for tile in unoccupied_tiles:
                i, j = tile[0], tile[1]
                modified_grid = [x.copy() for x in grid]
                modified_grid[i][j] = 1

                modified_unoccupied = unoccupied_tiles.copy()
                modified_unoccupied.remove(tile)

                evaluation = Bot.minimax(modified_grid, modified_unoccupied, False)
                max_evaluation = max(max_evaluation, evaluation)

            return max_evaluation
        else:
            min_evaluation = math.inf
            for tile in unoccupied_tiles:
                i, j = tile[0], tile[1]
                modified_grid = [x.copy() for x in grid]
                modified_grid[i][j] = -1

                modified_unoccupied = unoccupied_tiles.copy()
                modified_unoccupied.remove(tile)

                evaluation = Bot.minimax(modified_grid, modified_unoccupied, True)
                min_evaluation = min(min_evaluation, evaluation)

            return min_evaluation

    @staticmethod # recursive to handle outcome data in case the list is empty
    def get_choice_from_probability(probability):
        cumulative = 0.0
        num = random.random()
        for i, x in enumerate(probability):
            cumulative += x
            if num <= cumulative:
                return i