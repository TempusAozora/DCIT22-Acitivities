# py -3.12 main.py
# py -3.12 F:\DCIT22-Acitivities-main\TicTactoe\main.py
# py -3.12 F:\pygame\pygame_GUI\startingUI.py
import pygame
import sys
from tic_tac_toe import Game
from colors import *
from button import Button
from ScreenGUI import Gui

pygame.init()

screen_width = 750
screen_height = 550
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Tic Tac Toe")

clock = pygame.time.Clock()

background_image = pygame.image.load('./Images/Background_main.jpg').convert_alpha()
# logo = pygame.image.load('./Images/TicTacToe-remove
# bg-preview.png')

draw_surface = pygame.Surface((screen_width, screen_height), pygame.SRCALPHA)
draw_surface.fill((0, 0, 0, 0))

# FONTS CUSTOMIZED

BUTTON_FONT = pygame.font.Font('./Font/grobold/GROBOLD.ttf', 27)
BUTTON_FONT_MINI = pygame.font.Font('./Font/grobold/GROBOLD.ttf', 15)
# BUTTON_FONT = pygame.font.Font('./Font/compro_oro/Compro Oro.ttf', 27)

# BUTTON SETUP
start_button = Button(230, 250, 300, 80, "START", START_BUTTON_COLOR, START_BUTTON_HOVER_COLOR, BUTTON_FONT)
exit_button = Button(230, 340, 300, 80, "EXIT", EXIT_BUTTON_COLOR, EXIT_BUTTON_HOVER_COLOR, BUTTON_FONT)
simple_mode_button = Button(200, 250, 360, 80, "SIMPLE MODE", SIMPLE_MODE_BUTTON_COLOR, SIMPLE_MODE_BUTTON_HOVER_COLOR,
                            BUTTON_FONT)
ultimate_mode_button = Button(200, 340, 360, 80, "ULTIMATE TIC TAC TOE", MODIFIED_MODE_BUTTON_COLOR,
                              MODIFIED_MODE_BUTTON_HOVER_COLOR, BUTTON_FONT)
player_mode_button = Button(200, 250, 340, 80, "PLAYER VS PLAYER", PLAYER_MODE_BUTTON_COLOR,
                            PLAYER_MODE_BUTTON_HOVER_COLOR, BUTTON_FONT)
computer_mode_button = Button(200, 340, 340, 80, "COMPUTER VS PLAYER", COMPUTER_MODE_BUTTON_COLOR,
                              COMPUTER_MODE_BUTTON_HOVER_COLOR, BUTTON_FONT)
easy_mode_button = Button(200, 150, 340, 80, "EASY MODE", EASY_MODE_BUTTON_COLOR, EASY_MODE_BUTTON_HOVER_COLOR,
                          BUTTON_FONT)
medium_mode_button = Button(200, 250, 340, 80, "MEDIUM MODE", MEDIUM_BUTTON_COLOR, MEDIUM_BUTTON_HOVER_COLOR,
                            BUTTON_FONT)
hard_mode_button = Button(200, 350, 340, 80, "HARD MODE", HARD_MODE_BUTTON_COLOR, HARD_MODE_BUTTON_HOVER_COLOR,
                          BUTTON_FONT)
menu_button = Button(50, 450, 100, 50, "MENU", MENU_BUTTON_COLOR, MENU_BUTTON_HOVER_COLOR, BUTTON_FONT_MINI)
play_again_button = Button(575, 450, 120, 50, "PLAY AGAIN", PLAY_AGAIN_BUTTON_COLOR, PLAY_AGAIN_BUTTON_HOVER_COLOR, BUTTON_FONT_MINI)

game = Game(draw_surface)
current_gui = Gui("TIC TAC TOE",(180, 100),[start_button, exit_button])
previous_buttons = [start_button, exit_button]
bot_time_elapsed = 0

is_running = True
while is_running:
    mouse_position = pygame.mouse.get_pos()

    screen.blit(background_image, (-130, -220))
    # screen.blit(logo, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            # block input on bot delay
            if game.main_tic_tac_toe and not game.main_tic_tac_toe.finished:
                if game.bot and game.bot.bot_turn == True:
                    break
                elif game.bot:
                    bot_time_elapsed = pygame.time.get_ticks()

            # game inputs
            if game.is_running:
                game.input()

            # GUI inputs and behaviors
            if start_button.is_clicked(mouse_position):
                current_gui = Gui("MODE SELECTION", (130, 100), [simple_mode_button, ultimate_mode_button])
            elif exit_button.is_clicked(mouse_position):
                is_running = False
            elif simple_mode_button.is_clicked(mouse_position):
                current_gui = Gui("SIMPLE MODE", (180, 100), [player_mode_button, computer_mode_button])
            elif ultimate_mode_button.is_clicked(mouse_position):
                current_gui = Gui("ULTIMATE MODE", (140, 100), [player_mode_button, computer_mode_button])
            elif player_mode_button.is_clicked(mouse_position):
                mode = current_gui.text
                current_gui = Gui(buttons=[menu_button])
                if mode == "SIMPLE MODE":
                    game.set_mode("normal")
                elif mode == "ULTIMATE MODE":
                    game.set_mode("ultimate")

                game.init_game()
            elif computer_mode_button.is_clicked(mouse_position):
                mode = current_gui.text
                if mode == "SIMPLE MODE":
                    game.set_mode("normal")
                elif mode == "ULTIMATE MODE":
                    game.set_mode("ultimate")

                current_gui = Gui("COMPUTER DIFFICULTY", (50, 50),
                                  [easy_mode_button, medium_mode_button, hard_mode_button])
            elif easy_mode_button.is_clicked(mouse_position):
                game.init_game(difficulty="easy")
                current_gui = Gui(buttons=[menu_button])
            elif medium_mode_button.is_clicked(mouse_position):
                game.init_game(difficulty="medium")
                current_gui = Gui(buttons=[menu_button])
            elif hard_mode_button.is_clicked(mouse_position):
                game.init_game(difficulty="hard")
                current_gui = Gui(buttons=[menu_button])
            elif menu_button.is_clicked(mouse_position):
                draw_surface.fill((0, 0, 0, 0))
                game = Game(draw_surface)
                current_gui = Gui("TIC TAC TOE", (180, 100), [start_button, exit_button])
            elif play_again_button.is_clicked(mouse_position):

                # get previous data to make turns alternate
                next_turn = game.put_circle_main
                mode = game.mode
                difficulty = game.difficulty

                # reinitialize
                draw_surface.fill((0, 0, 0, 0))
                game = Game(draw_surface)
                game.put_circle_main = game.put_circle_mini = next_turn

                game.set_mode(mode)
                game.init_game(difficulty=difficulty)
                current_gui = Gui(buttons=[menu_button])

                # reset bot delay
                if game.bot:
                    bot_time_elapsed = pygame.time.get_ticks()
                    if not next_turn:
                        game.bot.bot_turn = True

    # bot put after delay
    current_time = pygame.time.get_ticks()
    if game.bot and game.bot.bot_turn and current_time - bot_time_elapsed >= game.bot.delay*1000:
        game.bot_put()

    # buttons that got hidden are automatically turned false
    if not current_gui or current_gui.buttons != previous_buttons:
        for button in previous_buttons:
            if button in current_gui.buttons:
                continue
            button.enabled = False

    # checks if in-game
    if game.main_tic_tac_toe:
        # if game finishes, gui will show "play again" button
        if game.main_tic_tac_toe.finished and game.is_running:
            current_gui = Gui(buttons=[menu_button, play_again_button])
            game.is_running = False

        # render game state
        game.render()
        screen.blit(draw_surface, (0,0))

    # render and update current gui
    if current_gui:
        current_gui.update()
        previous_buttons = current_gui.buttons
        current_gui.draw(screen=screen)

    pygame.display.update()
    clock.tick(60)

pygame.quit()
sys.exit()