import pygame
<<<<<<< HEAD
import math
from bot import Bot


from sound_manager import SoundManager
sfx = SoundManager()
=======

from sound_manager import SoundManager
sound = SoundManager()

# Tile class
class Tile:
    def __init__(self, i, j):
        self.position = (i, j)
        self.status = 0  # 1 for circle, 2 for cross

    def is_inside_the_tile(self, pos: tuple):
        return (self.position[0] - 0.5 < pos[0] < self.position[0] + 0.5 and
                self.position[1] - 0.5 < pos[1] < self.position[1] + 0.5)
>>>>>>> b3ab3177f80d748ab2779b0fdd2984c3d3f9f803

# Tic tac toe class
class TicTacToe:
    def __init__(self, size=200, position=(0, 0), destroy_on_finished=False, transparent_on_finished=False):
        self.size = size

        self.winner = 0
        self.finished = False

        self.position = position

        self.destroy_on_finished = destroy_on_finished
        self.transparent_on_finished = transparent_on_finished

<<<<<<< HEAD
        self.grid = [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]
        ]
=======
        self.tiles = []
        for i in range(-1, 2):
            for j in range(-1, 2):
                self.tiles.append(Tile(i, j))
>>>>>>> b3ab3177f80d748ab2779b0fdd2984c3d3f9f803

        self.matched_tiles = []
        self.occupied_tiles = 0

        self.grid_color = (255, 255, 255)
        self.circle_color = (0, 0, 255)
        self.cross_color = (255, 0, 0)
        self.matched_color = (0, 255, 0)

        self.line_thickness = 5

<<<<<<< HEAD
    def get_tile_from_mouse(self, screen):  # O(1)
        mouse_pos = pygame.mouse.get_pos()
        x, y = screen.get_size()

        grid_offset = (self.size / 2 - self.position[0], self.size / 2 - self.position[1])
        center_mouse_pos = (mouse_pos[0] - x / 2, mouse_pos[1] - y / 2)

        grid_pos = (
            math.floor((center_mouse_pos[0] + grid_offset[0]) / self.size * 3),
            math.floor((center_mouse_pos[1] + grid_offset[1]) / self.size * 3),
        )

        if 0 <= grid_pos[0] <= 2 and 0 <= grid_pos[1] <= 2:
            return grid_pos[1], grid_pos[0]
        else:
            return None, None

    def put_object_on_tile(self, screen, put_circle, index=None):  # when mouse is left-clicked.
        if index is not None:
            i, j = index[0], index[1]
        else:
            i, j = self.get_tile_from_mouse(screen)

        if i is not None and j is not None and self.grid[i][j] == 0:
            if put_circle:
                self.grid[i][j] = 1
            else:
                self.grid[i][j] = -1

            self.occupied_tiles += 1
            sfx.play_bubble_pop()

            self.matched_tiles, _ = self.check_game(self.grid)
            if len(self.matched_tiles) > 0:
                i, j = self.matched_tiles[0][0], self.matched_tiles[0][1]
                self.winner = self.grid[i][j]
                self.finished = True
            elif self.occupied_tiles == len(self.grid) ** 2:
                self.finished = True

            return True
        elif i is not None and j is not None:
            return "occupied"
        else:
            return None

    @staticmethod
    def check_game(grid):
        # Horizontal
        for i, row in enumerate(grid):
            if row[0] != 0 and (row[0] == row[1] and row[1] == row[2]):
                return ((i, 0), (i, 1), (i, 2)), grid[i][0]

        # Vertical
        for j in range(len(grid)):
            column = [row[j] for row in grid]
            if column[0] != 0 and (column[0] == column[1] and column[1] == column[2]):
                return ((0, j), (1, j), (2, j)), grid[0][j]

        # diagonal
        n = len(grid)
        diagonal = [grid[i][i] for i in range(n)]
        anti_diagonal = [grid[i][n - 1 - i] for i in range(n)]

        if diagonal[0] != 0 and (diagonal[0] == diagonal[1] and diagonal[1] == diagonal[2]):
            return ((0, 0), (1, 1), (2, 2)), grid[0][0]
        elif anti_diagonal[0] != 0 and (anti_diagonal[0] == anti_diagonal[1] and anti_diagonal[1] == anti_diagonal[2]):
            return ((0, 2), (1, 1), (2, 0)), grid[0][2]

        return (), 0
=======
    def get_tile_from_mouse(self, screen):  # O(n)
        x, y = screen.get_size()
        mouse_pos = pygame.mouse.get_pos()
        offset_center = (x / 2 + self.position[0], y / 2 + self.position[1])

        rel_mouse_pos = (
            (mouse_pos[0] - offset_center[0]) / (self.size * 2 / 3),
            (mouse_pos[1] - offset_center[1]) / (self.size * 2 / 3)
        )

        for tile in self.tiles:
            if tile.is_inside_the_tile(rel_mouse_pos):
                return tile

        return None

    def put_object_on_tile(self, screen, put_circle, tile_index=None):  # when mouse is left-clicked.
        if tile_index is not None:
            clicked_tile = self.tiles[tile_index]
            if clicked_tile and clicked_tile.status == 0:
                if put_circle:
                    clicked_tile.status = 1
                else:
                    clicked_tile.status = 2

                self.occupied_tiles += 1
                self.check_game()

                return True
            elif clicked_tile:
                return "occupied"
        else:
            clicked_tile = self.get_tile_from_mouse(screen)
            if clicked_tile and clicked_tile.status == 0:
                if put_circle:
                    clicked_tile.status = 1
                else:
                    clicked_tile.status = 2

                self.occupied_tiles += 1
                self.check_game()

                return True
            elif clicked_tile:
                return "occupied"

        return None

    def check_game(self):
        # vertical
        matched_tiles: list = []
        for i in range(3):
            if self.tiles[i * 3].status == 0:
                continue
            if self.tiles[i * 3].status == self.tiles[1 + i * 3].status and self.tiles[1 + i * 3].status == self.tiles[
                2 + i * 3].status:
                matched_tiles = [self.tiles[i * 3], self.tiles[1 + i * 3], self.tiles[2 + i * 3]]
                break

        # Horizontal
        if len(matched_tiles) == 0:
            for i in range(3):
                if self.tiles[i].status == 0:
                    continue
                if self.tiles[i].status == self.tiles[i + 3].status and self.tiles[i + 3].status == self.tiles[
                    i + 6].status:
                    matched_tiles = [self.tiles[i], self.tiles[i + 3], self.tiles[i + 6]]
                    break

        # diagonal
        if len(matched_tiles) == 0:
            if self.tiles[0].status != 0 and self.tiles[0].status == self.tiles[4].status and self.tiles[4].status == \
                    self.tiles[8].status:
                matched_tiles = [self.tiles[0], self.tiles[4], self.tiles[8]]
            elif self.tiles[2].status != 0 and self.tiles[2].status == self.tiles[4].status and self.tiles[4].status == \
                    self.tiles[6].status:
                matched_tiles = [self.tiles[2], self.tiles[4], self.tiles[6]]

        self.matched_tiles = matched_tiles

        if len(matched_tiles) > 0:
            start_tile = matched_tiles[0]
            self.winner = start_tile.status
            self.finished = True
        elif self.occupied_tiles == len(self.tiles):
            self.finished = True
>>>>>>> b3ab3177f80d748ab2779b0fdd2984c3d3f9f803

    def draw(self, screen):
        x, y = screen.get_size()
        offset_center = (x / 2 + self.position[0], y / 2 + self.position[1])
<<<<<<< HEAD
        offset = (offset_center[0] - self.size / 3, offset_center[1] - self.size / 3)
=======
>>>>>>> b3ab3177f80d748ab2779b0fdd2984c3d3f9f803

        alpha = 255
        if self.finished and self.transparent_on_finished:
            alpha = 50

        # create grid
        for x in (-1, 1):
            pygame.draw.line(
                screen,
                self.grid_color + (alpha,),
<<<<<<< HEAD
                (self.size / 2 * x / 3 + offset_center[0], self.size / 2 + offset_center[1]),
                (self.size / 2 * x / 3 + offset_center[0], -self.size / 2 + offset_center[1]),
=======
                (self.size * x / 3 + offset_center[0], self.size + offset_center[1]),
                (self.size * x / 3 + offset_center[0], -self.size + offset_center[1]),
>>>>>>> b3ab3177f80d748ab2779b0fdd2984c3d3f9f803
                width=self.line_thickness
            )

        for y in (-1, 1):
            pygame.draw.line(
                screen,
                self.grid_color + (alpha,),
<<<<<<< HEAD
                (self.size / 2 + offset_center[0], self.size / 2 * y / 3 + offset_center[1]),
                (-self.size / 2 + offset_center[0], self.size / 2 * y / 3 + offset_center[1]),
=======
                (self.size + offset_center[0], self.size * y / 3 + offset_center[1]),
                (-self.size + offset_center[0], self.size * y / 3 + offset_center[1]),
>>>>>>> b3ab3177f80d748ab2779b0fdd2984c3d3f9f803
                width=self.line_thickness
            )

        # create circles or cross on the grid
<<<<<<< HEAD
        for x in range(3):
            for y in range(3):
                if self.grid[y][x] == 1:
                    pos = (x * self.size / 2 * (2 / 3) + offset[0],
                           y * self.size / 2 * (2 / 3) + offset[1])
                    pygame.draw.circle(screen, self.circle_color + (alpha,), pos, self.size / 8, self.line_thickness)

                elif self.grid[y][x] == -1:
                    pos = (x * self.size / 2 * (2 / 3) + offset[0],
                           y * self.size / 2 * (2 / 3) + offset[1])
                    pygame.draw.line(
                        screen,
                        self.cross_color + (alpha,),
                        (pos[0] + self.size / 8, pos[1] + self.size / 8),
                        (pos[0] - self.size / 8, pos[1] - self.size / 8),
                        width=self.line_thickness
                    )
                    pygame.draw.line(
                        screen,
                        self.cross_color + (alpha,),
                        (pos[0] - self.size / 8, pos[1] + self.size / 8),
                        (pos[0] + self.size / 8, pos[1] - self.size / 8),
                        width=self.line_thickness
                    )

        # draw line when game ended
        if len(self.matched_tiles) > 0:
            start_y, start_x = self.matched_tiles[0][0], self.matched_tiles[0][1]
            end_y, end_x = self.matched_tiles[-1][0], self.matched_tiles[-1][1]
            start_pos = (start_x * self.size / 2 * (2 / 3) + offset[0],
                         start_y * self.size / 2 * (2 / 3) + offset[1])
            end_pos = (end_x * self.size / 2 * (2 / 3) + offset[0],
                       end_y * self.size / 2 * (2 / 3) + offset[1])
=======
        for tile in self.tiles:
            if tile.status == 1:
                pos = (tile.position[0] * self.size * (2 / 3) + offset_center[0],
                       tile.position[1] * self.size * (2 / 3) + offset_center[1])
                pygame.draw.circle(screen, self.circle_color + (alpha,), pos, self.size / 4, self.line_thickness)

            elif tile.status == 2:
                pos = (tile.position[0] * self.size * (2 / 3) + offset_center[0],
                       tile.position[1] * self.size * (2 / 3) + offset_center[1])
                pygame.draw.line(
                    screen,
                    self.cross_color + (alpha,),
                    (pos[0] + self.size / 4, pos[1] + self.size / 4),
                    (pos[0] - self.size / 4, pos[1] - self.size / 4),
                    width=self.line_thickness
                )
                pygame.draw.line(
                    screen,
                    self.cross_color + (alpha,),
                    (pos[0] - self.size / 4, pos[1] + self.size / 4),
                    (pos[0] + self.size / 4, pos[1] - self.size / 4),
                    width=self.line_thickness
                )

        # draw line when game ended
        if len(self.matched_tiles) > 0:
            start_tile = self.matched_tiles[0]
            end_tile = self.matched_tiles[-1]
            start_pos = (start_tile.position[0] * self.size * (2 / 3) + offset_center[0],
                         start_tile.position[1] * self.size * (2 / 3) + offset_center[1])
            end_pos = (end_tile.position[0] * self.size * (2 / 3) + offset_center[0],
                       end_tile.position[1] * self.size * (2 / 3) + offset_center[1])
>>>>>>> b3ab3177f80d748ab2779b0fdd2984c3d3f9f803

            pygame.draw.line(
                screen,
                self.matched_color + (alpha,),
                start_pos,
                end_pos,
                width=self.line_thickness
            )

<<<<<<< HEAD

=======
>>>>>>> b3ab3177f80d748ab2779b0fdd2984c3d3f9f803
class Game:
    def __init__(self, screen):
        self.screen = screen
        self.mode = None
<<<<<<< HEAD
        self.bot = None
        self.difficulty = None
=======
>>>>>>> b3ab3177f80d748ab2779b0fdd2984c3d3f9f803

        self.main_tic_tac_toe = None
        self.mini_tic_tac_toe = None

        self.put_circle_main = True
        self.put_circle_mini = True

<<<<<<< HEAD
        self.is_running = False

        self.mini_tile_input_coords = (0,0) # the bot will stick to the mini tic-tac-toe that has received input.

    def set_mode(self, mode):
        self.mode = mode

    def init_game(self, difficulty=None):
        if self.mode == "normal":
            self.difficulty = difficulty
            self.normal_mode_init(difficulty)
        elif self.mode == "ultimate":
            self.difficulty = difficulty
            self.ultimate_mode_init(difficulty)
        else:
            print("Set mode first")

    def normal_mode_init(self, difficulty=None):
        self.main_tic_tac_toe = TicTacToe(size=300, position=(0, 30))
        self.mode = "normal"

        if difficulty is not None:
            self.bot = Bot(-1, difficulty=difficulty)
        else:
            self.bot = None

        self.is_running = True

    def ultimate_mode_init(self, difficulty=None):
        data = {"size": 400, "position": (0, 50)}

        tic_tac_toe_objects = []
        for i in range(3):
            row = []
            for j in range(3):
                mini_tic_tac_toe = TicTacToe(size=data["size"] // 4, position=(
                data["size"] / 2 * (2 / 3) * j + data["position"][0] - data["size"] / 3,
                data["size"] / 2 * (2 / 3) * i + data["position"][1] - data["size"] / 3
                ),
                                             transparent_on_finished=True)
                row.append(mini_tic_tac_toe)

            tic_tac_toe_objects.append(row)
=======
    def normal_mode_init(self):
        self.main_tic_tac_toe = TicTacToe(size=150, position=(0,50))
        self.mode = "normal"

    def ultimate_mode_init(self):
        data = {"size": 200, "position": (0,50)}

        tic_tac_toe_objects = []
        for i in range(-1, 2):
            for j in range(-1, 2):
                mini_tic_tac_toe = TicTacToe(size=data["size"]/4, position=(data["size"] * 2/3 * i + data["position"][0], data["size"] * 2/3 * j + data["position"][1]), transparent_on_finished=True)
                tic_tac_toe_objects.append(mini_tic_tac_toe)
>>>>>>> b3ab3177f80d748ab2779b0fdd2984c3d3f9f803

        self.main_tic_tac_toe = TicTacToe(size=data["size"], position=data["position"])
        self.mini_tic_tac_toe = tic_tac_toe_objects
        self.mode = "ultimate"

<<<<<<< HEAD
        if difficulty is not None:
            self.bot = Bot(-1, difficulty=difficulty)
        else:
            self.bot = None

        self.is_running = True

=======
>>>>>>> b3ab3177f80d748ab2779b0fdd2984c3d3f9f803
    def input(self):
        if self.main_tic_tac_toe.finished:
            return

<<<<<<< HEAD
        def put_on_main_tile(put_circle: bool = self.put_circle_main, chosen_tile=None):
            has_put = self.main_tic_tac_toe.put_object_on_tile(self.screen, put_circle, chosen_tile)
            if has_put and has_put != "occupied":
                self.put_circle_main = not put_circle
                return True
            return None

        if self.mode == "normal":
            has_put_in_tile = put_on_main_tile()
            if not self.bot or not has_put_in_tile:
                return

            self.bot.bot_turn = True

        elif self.mode == "ultimate":
            for i, row in enumerate(self.mini_tic_tac_toe):
                for j, t in enumerate(row):
                    if t.finished:
                        continue

                    has_put_in_tile = t.put_object_on_tile(self.screen, self.put_circle_mini)
                    if has_put_in_tile:
                        if has_put_in_tile == "occupied":
                            return

                        self.put_circle_mini = not self.put_circle_mini
                        if t.finished:
                            if t.winner == 1:
                                put_on_main_tile(True)
                            elif t.winner == -1:
                                put_on_main_tile(False)
                            else:
                                put_on_main_tile()

                            if self.main_tic_tac_toe.finished:
                                return

                        if self.bot:
                            self.bot.bot_turn = True

                        self.mini_tile_input_coords = (i,j)

                        return

    def bot_put(self):
        if self.main_tic_tac_toe.finished:
            return

        if self.mode == "normal":
            choice = self.bot.choose(self.main_tic_tac_toe.grid)
            self.main_tic_tac_toe.put_object_on_tile(self.screen, self.put_circle_main, choice)
            self.put_circle_main = not self.put_circle_main
            self.bot.bot_turn = False
        elif self.mode == "ultimate":
            choice = self.mini_tile_input_coords
            i_, j_ = choice[0], choice[1]
            if self.mini_tic_tac_toe[i_][j_].finished:
                choice = self.bot.choose(self.main_tic_tac_toe.grid)
                i_,j_ = choice[0], choice[1]

            chosen_mini = self.mini_tic_tac_toe[i_][j_]
            choice_from_chosen_mini = self.bot.choose(chosen_mini.grid)
            chosen_mini.put_object_on_tile(self.screen, self.put_circle_mini, choice_from_chosen_mini)

            self.put_circle_mini = not self.put_circle_mini
            if chosen_mini.finished:
                if chosen_mini.winner == 1:
                    self.main_tic_tac_toe.put_object_on_tile(self.screen, True, choice)
                    self.put_circle_main = False
                elif chosen_mini.winner == -1:
                    self.main_tic_tac_toe.put_object_on_tile(self.screen, False, choice)
                    self.put_circle_main = True
                else:
                    self.main_tic_tac_toe.put_object_on_tile(self.screen, self.put_circle_main, choice)
                    self.put_circle_main = not self.put_circle_main

            self.bot.bot_turn = False

    def render(self):
=======
        def put_on_main_tile(put_circle: bool = self.put_circle_main):
            has_put = self.main_tic_tac_toe.put_object_on_tile(self.screen, put_circle)
            if has_put and has_put != "occupied":
                self.put_circle_main = not put_circle
                sound.play_click()

        if self.mode == "normal":
            put_on_main_tile()

        elif self.mode == "ultimate":
            for i, t in enumerate(self.mini_tic_tac_toe):
                if t.finished:
                    continue

                has_put_in_tile = t.put_object_on_tile(self.screen, self.put_circle_mini)
                if has_put_in_tile:
                    if has_put_in_tile == "occupied":
                        break

                    self.put_circle_mini = not self.put_circle_mini
                    sound.play_click()
                    if t.finished:
                        if t.winner == 1:
                            put_on_main_tile(True)
                        elif t.winner == 2:
                            put_on_main_tile(False)
                        else:
                            put_on_main_tile()

                    break

    def update(self):
>>>>>>> b3ab3177f80d748ab2779b0fdd2984c3d3f9f803
        if self.main_tic_tac_toe:
            self.main_tic_tac_toe.draw(self.screen)

        if self.mini_tic_tac_toe:
<<<<<<< HEAD
            for row in self.mini_tic_tac_toe:
                for t in row:
                    t.draw(self.screen)

            self.main_tic_tac_toe.draw(self.screen)
=======
            for t in self.mini_tic_tac_toe:
                t.draw(self.screen)

            self.main_tic_tac_toe.draw(self.screen)

>>>>>>> b3ab3177f80d748ab2779b0fdd2984c3d3f9f803
