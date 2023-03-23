import pygame

class Gran():
    def __init__(self, screen ):
        self.screen = screen
        self.image = pygame.image.load("nikita/pixil-frame-0.png")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx

        self.center = float(self.rect.centerx)
        self.rect.bottom = self.screen_rect.bottom
        self.mright = False
        self.mleft = False
    def output(self):

        self.screen.blit(self.image, self.rect)
    def up(self):
        if self.mright and self.rect.right < self.screen_rect.right:
            self.center += 4
        elif self.mleft and self.rect.left > 0:
            self.center += -4
        self.rect.centerx = self.center