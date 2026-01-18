import pygame
from colors import *
import sound_manager

class Button():
    def __init__(self, x, y, width, height, text, color, hover_color, font):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.color = color
        self.hover_color = hover_color
        self.current_color = color
        self.font = font
        self.enabled = False

    def draw_button_sets(self, surface):
        # BUTTON SHADOW
        shadow_rect = self.rect.copy()
        shadow_rect.y += 5
        pygame.draw.rect(surface, DARK_GRAY, shadow_rect, border_radius=20)

        # BUTTON AND BORDER
        pygame.draw.rect(surface, self.current_color, self.rect, border_radius=20)  # BUTTON
        pygame.draw.rect(surface, WHITE, self.rect, 1, border_radius=20)  # BORDER

        # TEXT
        text_surface = self.font.render(self.text, True, WHITE)
        text_rect = text_surface.get_rect(center=self.rect.center)
        surface.blit(text_surface, text_rect)

    def button_update(self, mouse_position):
        if self.rect.collidepoint(mouse_position):
            self.current_color = self.hover_color
        else:
            self.current_color = self.color

    def is_clicked(self, mouse_position):
        if self.enabled:
            if self.rect.collidepoint(mouse_position):
                sound_manager.click_sound.play()
            return self.rect.collidepoint(mouse_position)
        else:
            return False

pygame.font.init()
# FONTS CUSTOMIZED
BUTTON_FONT = pygame.font.Font('./Font/grobold/GROBOLD.ttf', 27)
BUTTON_FONT_MINI = pygame.font.Font('./Font/grobold/GROBOLD.ttf', 15)

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

