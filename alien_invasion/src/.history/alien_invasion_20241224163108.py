import sys
import pygame


class AlienInvasion:
    """管理游戏资源和行为的类"""
    
    def __init__(self):
        """初始化游戏并创建游戏资源"""
        pygame.init()
        
        self.screen = pygame.display.set_mode((1200, 800))
        self.clock = pygame.time.clock()
        pygame.display.set_caption("Alien Invasion")
        
    def run_game(self):
        """开始游戏的主循环"""
        while True:
            for event in pygame.event.get(): # 事件循环
                print(event)
                if event.type == pygame.QUIT:  # 用户点击退出按钮
                    sys.exit()
                    
                    
            # 让最近绘制的屏幕可见 》》》 堆叠图层，只向用户展示新屏幕
            pygame.display.flip()
            
            
# ! 仅当直接运行该py文件时，才会执行下面代码
if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()




