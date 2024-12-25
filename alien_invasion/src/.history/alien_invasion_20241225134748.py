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
            for event in pygame.event.get(): # 事件循环
                # print(event)
                if event.type == pygame.QUIT:  # 用户点击退出按钮
                    sys.exit()
                    
                    
            # 每次循环重新 绘制屏幕 
            self.screen.fill(self.settings.bg_color)
            self.ship.blitme()
            
            # 让最近绘制的屏幕可见 》》》 堆叠图层，只向用户展示新屏幕
            pygame.display.flip()
            self.clock.tick(60) # 每秒60帧
            
            
    def _check_events(self):
        """响应按键和鼠标事件, 将"""
        for event in pygame.event.get():
            
            
# ! 仅当直接运行该py文件时，才会执行下面代码
if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()



