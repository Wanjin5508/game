import sys
import pygame

from settings import Settings
from ship import Ship 
from bullet import Bullet

class AlienInvasion:
    """管理游戏资源和行为的类"""
    
    def __init__(self):
        """初始化游戏并创建游戏资源"""
        pygame.init()
        
        # self.screen = pygame.display.set_mode((1200, 800))
        
        self.settings = Settings()
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        
        self.clock = pygame.time.Clock()
        
        pygame.display.set_caption("Alien Invasion")
        
        # ! 创建实例, 并传入self
        self.ship = Ship(self)
        
        self.bullets = pygame.sprite.Group()  # * 数据结构用于存储一组子弹
        

        
    def run_game(self):
        """开始游戏的主循环"""
        while True:
            # * 使用helper method简化主循环
            self._check_events()
            self.ship.update()
            self.bullets.update()
            self._update_screen()
            
            self.clock.tick(60) # 每秒60帧
            
            
    def _check_events(self):
        """响应按键和鼠标事件, 将事件检验和屏幕更新分离"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            # * 按下键盘事件
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            # * 松开键盘事件
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
            
            
    def _check_keydown_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True 
        elif event.key == pygame.K_ESCAPE:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet
                
    def _check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False
            
    def _update_screen(self):
        """更新屏幕上的图像, 并切换到新屏幕"""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        pygame.display.flip()
            
# ! 仅当直接运行该py文件时，才会执行下面代码
if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()




