import sys
import pygame

from settings import Settings
from ship import Ship 

class AlienInvasion:
    """管理游戏资源和行为的类"""
    
    def __init__(self):
        """初始化游戏并创建游戏资源"""
        pygame.init()
        
        # self.screen = pygame.display.set_mode((1200, 800))
        
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        
        self.clock = pygame.time.Clock()
        
        pygame.display.set_caption("Alien Invasion")
        
        # ! 创建实例, 并传入self
        self.ship = Ship(self)
        

        
    def run_game(self):
        """开始游戏的主循环"""
        while True:
            self._check_events()
                    
                    
            # 每次循环重新 绘制屏幕 
            self.screen.fill(self.settings.bg_color)
            self.ship.blitme()
            
            # 让最近绘制的屏幕可见 》》》 堆叠图层，只向用户展示新屏幕
            pygame.display.flip()
            self.clock.tick(60) # 每秒60帧
            
            
    def _check_events(self):
        """响应按键和鼠标事件, 将事件检验和屏幕更新分离"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            
            
    def _update
            
# ! 仅当直接运行该py文件时，才会执行下面代码
if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()




