# py -3.12 main.py
# py -3.12 F:\DCIT22-Acitivities-main\TicTactoe\main.py
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
draw_surface.fill((0,0,0,0))

#FONTS CUSTOMIZED

BUTTON_FONT = pygame.font.Font('./Font/grobold/GROBOLD.ttf', 27)
# BUTTON_FONT = pygame.font.Font('./Font/compro_oro/Compro Oro.ttf', 27)

#BUTTON SETUP
start_button = Button(230, 250, 300, 80, "START", START_BUTTON_COLOR, START_BUTTON_HOVER_COLOR, BUTTON_FONT)
exit_button = Button(230, 340, 300, 80, "EXIT", EXIT_BUTTON_COLOR, EXIT_BUTTON_HOVER_COLOR, BUTTON_FONT)
simple_mode_button = Button(200, 250, 360, 80, "SIMPLE MODE", SIMPLE_MODE_BUTTON_COLOR, SIMPLE_MODE_BUTTON_HOVER_COLOR, BUTTON_FONT)
ultimate_mode_button = Button(200, 340, 360, 80, "ULTIMATE TIC TAC TOE", MODIFIED_MODE_BUTTON_COLOR, MODIFIED_MODE_BUTTON_HOVER_COLOR, BUTTON_FONT)
player_mode_button = Button(200, 250, 340, 80, "PLAYER VS PLAYER", PLAYER_MODE_BUTTON_COLOR, PLAYER_MODE_BUTTON_HOVER_COLOR, BUTTON_FONT)
computer_mode_button = Button(200, 340, 340, 80, "COMPUTER VS PLAYER", COMPUTER_MODE_BUTTON_COLOR, COMPUTER_MODE_BUTTON_HOVER_COLOR, BUTTON_FONT)
easy_mode_button = Button(200, 150, 340, 80, "EASY MODE", EASY_MODE_BUTTON_COLOR, EASY_MODE_BUTTON_HOVER_COLOR, BUTTON_FONT)
medium_mode_button = Button(200, 250, 340, 80, "MEDIUM MODE", MEDIUM_BUTTON_COLOR, MEDIUM_BUTTON_HOVER_COLOR, BUTTON_FONT)
hard_mode_button = Button(200, 350, 340, 80, "HARD MODE", HARD_MODE_BUTTON_COLOR, HARD_MODE_BUTTON_HOVER_COLOR, BUTTON_FONT)

# state_m = "start"
game = Game(draw_surface)

current_gui = Gui("TIC TAC TOE",(180, 100),[start_button, exit_button])
previous_buttons = [start_button, exit_button]

is_running = True
while is_running:
    mouse_position = pygame.mouse.get_pos()

    screen.blit(background_image, (-130, -220))
    # screen.blit(logo, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
                if start_button.is_clicked(mouse_position):
                    
                    current_gui = Gui("MODE SELECTION",(130, 100),[simple_mode_button, ultimate_mode_button])
                    print("CLICK")
                elif exit_button.is_clicked(mouse_position):
                    is_running = False
                elif simple_mode_button.is_clicked(mouse_position):
                    current_gui = Gui("SIMPLE MODE",(180,100),[player_mode_button, computer_mode_button])
                elif ultimate_mode_button.is_clicked(mouse_position):
                    current_gui = Gui("ULTIMATE MODE",(140,100),[player_mode_button, computer_mode_button])
            
                elif player_mode_button.is_clicked(mouse_position):
                    print("PLAYER MODE")
                elif computer_mode_button.is_clicked(mouse_position):
                    current_gui = Gui("COMPUTER DIFFICULTY",(50,50),[easy_mode_button, medium_mode_button, hard_mode_button])
                    print("COMPUTER MODE")
                elif easy_mode_button.is_clicked(mouse_position):
                    print("EASY MODE!")
                elif medium_mode_button.is_clicked(mouse_position):
                    print("MEDIUM MODE!")
                elif hard_mode_button.is_clicked(mouse_position):
                    print("HARD MODE!")    

    if current_gui.buttons != previous_buttons:
        for button in previous_buttons:
            button.enabled = False
    
    current_gui.update()
    previous_buttons = current_gui.buttons
    # screen.fill(DARK_NAVY)
    current_gui.draw(screen=screen)

    pygame.display.update()
    clock.tick(60)
    
pygame.quit()
sys.exit()