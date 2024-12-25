import sys
import pygame

from settings import Settings
from ship import Ship 
from bullet import Bullet
from alien import Alien 

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
        self.aliens = pygame.sprite.Group()
        self._create_fleet()
        

        
    def run_game(self):
        """开始游戏的主循环"""
        while True:
            # * 使用helper method简化主循环
            self._check_events()
            self.ship.update()
            
            self._update_bullets()
            self._update_aliens()
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
            self._fire_bullet()
                
    def _check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False
            
    def _fire_bullet(self):
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)
            
    def _update_bullets(self):
        self.bullets.update()
            
        # * 删除已经位于屏幕 外面的子弹
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
        # print(len(self.bullets))
        
        # J
        
    def _update_aliens(self):
        self._check_fleet_edges()
        self.aliens.update()
        
    def _create_fleet(self):
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size 
        current_x, current_y = alien_width, alien_height
        while current_y < (self.settings.screen_height - 3 * alien_height):
            while current_x < (self.settings.screen_width - 2 * alien_width):
                self._create_alien(current_x, current_y)
                current_x += 2 * alien_width
                
            
            # * 添加一行外星人后，重置x并递增y
            current_x = alien_width
            current_y += 2 * alien_height
        
                
    def _create_alien(self, x_position, y_position):
        new_alien = Alien(self)
        new_alien.x = x_position
        new_alien.rect.x = x_position
        new_alien.rect.y = y_position
        self.aliens.add(new_alien)
        
        
    def _check_fleet_edges(self):
        """有外星人到达边缘时采取相应措施"""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break
                
    def _change_fleet_direction(self):
        """将整群外星人下移，并改变方向"""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1
            
    def _update_screen(self):
        """更新屏幕上的图像, 并切换到新屏幕"""
        self.screen.fill(self.settings.bg_color)
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.ship.blitme()
        self.aliens.draw(self.screen)
        pygame.display.flip()
            
# ! 仅当直接运行该py文件时，才会执行下面代码
if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()




