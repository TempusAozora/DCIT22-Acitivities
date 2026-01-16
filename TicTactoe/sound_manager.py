import pygame

class SoundManager:
    def __init__(self):
        pygame.mixer.init()
        self.click_sound = pygame.mixer.Sound("./sound/click_button.wav")
<<<<<<< HEAD
        self.click_sound.set_volume(0.5)

        self.bubble_pop_sound = pygame.mixer.Sound("./sound/bubble_pop.mp3")
        self.bubble_pop_sound.set_volume(0.5)

    def play_click(self):
        self.click_sound.play()

    def play_bubble_pop(self):
        self.bubble_pop_sound.play()
=======

        self.click_sound.set_volume(0.5)

    def play_click(self):
        self.click_sound.play()
>>>>>>> f357de79b485dd07e713abf682daa3590fdabc09
