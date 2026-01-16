import pygame
from colors import *

<<<<<<< HEAD
class Gui:
    def __init__(self, text="", header_position=(0, 0), buttons=[]):
        self.header_position = header_position
        self.buttons = buttons
        self.text = text

        for button in self.buttons:
            button.enabled = True

=======
class Gui():
    def __init__(self, text="", header_position=(0,0), buttons=[]):
        self.header_position = header_position
        self.buttons = buttons  
        self.text = text
        for button in self.buttons:
            button.enabled = True
            
>>>>>>> f357de79b485dd07e713abf682daa3590fdabc09
    def update(self):
        mouse_position = pygame.mouse.get_pos()
        for button in self.buttons:
            button.button_update(mouse_position)
<<<<<<< HEAD

=======
            
>>>>>>> f357de79b485dd07e713abf682daa3590fdabc09
    def draw(self, screen):
        Header_title = pygame.font.Font('./Font/kids_magazine/Kids Magazine.ttf', 40)
        header = Header_title.render(self.text, True, WHITE)

        screen.blit(header, (self.header_position[0], self.header_position[1]))
        for button in self.buttons:
            button.draw_button_sets(screen)
<<<<<<< HEAD
=======
        
>>>>>>> f357de79b485dd07e713abf682daa3590fdabc09
