

import pygame

class Ship:
    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        
        # Load the ship image and get its rect.
        self.image = pygame.image.load("images\ship.bmp")
        self.rect = self.image.get_rect()
        
        # Start each new ship at the bottom center of the screen.
        