import sys

import pygame 

class AlienInvasion:
    """管理游戏资源和行为的类"""
    
    def __init__(self):
        """初始化游戏并创建游戏资源"""
        pygame.init()
        
        self.screen = pygamenp.display.set_mode((1200, 800))
        pygame.display.set_caption("Alien Invasion")
        
    def run_game(self):
        """开始游戏的主循环"""
        while True:
            for event in pygame.event.get




