import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen 
        self.image = pygame.image.load("images/alien.bmp")
        
        self.rect = self.image.get_rect()
        self.settings = ai_game.settings
        
        # * 每个外星人出现在屏幕的左上角
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        
        # 存储外星人的精确水平位置
        self.x = float(self.rect.x)
        
    def update(self):
        # * 外星人向右移动
        self.x += self.settings.alien_speed
        self.rect.x = self.x

    def check_edges(self):
        # * 如果外星人到达屏幕边缘，就返回True
        screen_rect = self.screen.get_rect()
        return 