# py -3.12 main.py
# py -3.12 F:\DCIT22-Acitivities-main\TicTactoe\main.py
# py -3.12 F:\pygame\pygame_GUI\startingUI.py
import sys
from tic_tac_toe import Game
from button import *
from ScreenGUI import Gui
import pygame

pygame.init()

screen_width = 750
screen_height = 550
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Tic Tac Toe")

clock = pygame.time.Clock()

background_image = pygame.image.load('./Images/Background_main.jpg').convert_alpha()
draw_surface = pygame.Surface((screen_width, screen_height), pygame.SRCALPHA)
draw_surface.fill((0, 0, 0, 0))

game = Game(draw_surface)
current_gui = Gui("TIC TAC TOE",(180, 100),[start_button, exit_button])

previous_buttons = [start_button, exit_button]
bot_time_elapsed = 0

is_running = True
while is_running:
    mouse_position = pygame.mouse.get_pos()
    screen.blit(background_image, (-130, -220))

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
                game.set_mode("normal")
            elif ultimate_mode_button.is_clicked(mouse_position):
                current_gui = Gui("ULTIMATE MODE", (140, 100), [player_mode_button, computer_mode_button])
                game.set_mode("ultimate")
            elif player_mode_button.is_clicked(mouse_position):
                current_gui = Gui(buttons=[menu_button])
                game.init_game()
            elif computer_mode_button.is_clicked(mouse_position):
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

            winner = game.main_tic_tac_toe.winner #1 - circle, 0 draw, -1 x,
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