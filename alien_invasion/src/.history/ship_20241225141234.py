

import pygame

class Ship:
    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.settings
        
        # Load the ship image and get its rect.
        self.image = pygame.image.load("images\ship.bmp")
        self.rect = self.image.get_rect()
        
        # Start each new ship at the bottom center of the screen.
        self.rect.midbottom = self.screen_rect.midbottom
        
        self.x = float(self.rect.x)
        
        # 添加移动属性
        self.moving_right = False
        self.moving_left = False
        
    def blitme(self):
        # 在指定位置绘制飞船
        self.screen.blit(self.image, self.rect)
        
    def update(self):
        # 根据移动方向更新飞船位置
        if self.moving_right:
            self.x += self.settings.ship_speed
        if self.moving_left:        # ! 注意不能使用elif
            self.x -= self.settings.ship_speed
            
        self.rectf.