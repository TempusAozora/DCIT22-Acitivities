import pygame

class SoundManager:
    def __init__(self):
        pygame.mixer.init()
        self.click_sound = pygame.mixer.Sound("./sound/click_button.wav")

        self.click_sound.set_volume(0.5)

    def play_click(self):
        self.click_sound.play()
