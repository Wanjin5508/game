import sys
import pygame

from settings import Settings

class AlienInvasion:
    """管理游戏资源和行为的类"""
    
    def __init__(self):
        """初始化游戏并创建游戏资源"""
        pygame.init()
        
        # self.screen = pygame.display.set_mode((1200, 800))
        
        self.settings = Settings()
        self.clock = pygame.time.clock()
        
        pygame.display.set_caption("Alien Invasion")
        
        # 设置背景色
        self.bg_color = (230, 230, 230)
        
    def run_game(self):
        """开始游戏的主循环"""
        while True:
            for event in pygame.event.get(): # 事件循环
                print(event)
                if event.type == pygame.QUIT:  # 用户点击退出按钮
                    sys.exit()
                    
                    
            # 每次循环重新 绘制屏幕 
            self.screen.fill(self.bg_color)
            
            # 让最近绘制的屏幕可见 》》》 堆叠图层，只向用户展示新屏幕
            pygame.display.flip()
            self.clock.tick(60) # 每秒60帧
            
            
# ! 仅当直接运行该py文件时，才会执行下面代码
if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()




