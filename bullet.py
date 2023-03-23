import pygame

class Bullet(pygame.sprite.Sprite):
    def __init__(self, screen, hi):
        super(Bullet, self).__init__()
        self.screen = screen
        self.rect = pygame.Rect(0, 0, 5, 12)
        self.color = 139, 195, 56
        self.speed = 4
        self.rect.centerx = hi.rect.centerx
        self.rect.top = hi.rect.top
        self.y = float(self.rect.y)

    def update(self):
        self.y -= self.speed
        self.rect.y = self.y
    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)