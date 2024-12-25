import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen 
        self.image = pygame.image.load("images/alien.bmp")
        
        self.rect = self.image.get_rect()
        
        # * 每个外星人出现在屏幕的左上角
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        
        # 存储外星人的精确水平位置
        self.x = float(self.rect.x)
        
    def update(self):
        

