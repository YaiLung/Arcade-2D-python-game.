import pygame
import controls
from nikitagan import  Gran
from pygame.sprite import Group

def run():

    pygame.init()

    screen = pygame.display.set_mode((800,1000))
    pygame.display.set_caption("игра говна")
    bg_color = pygame.image.load("nikita/pxArt.png")

    hi = Gran(screen)
    bullets = Group()
    inos = Group()
    controls.create_army(screen, inos)

    while True:
        screen.blit(bg_color,(0,0))


        controls.events(screen, hi, bullets)
        hi.up()
        bullets.update()
        controls.update(bg_color, screen, hi, inos, bullets)
        controls.update_bullets(inos, bullets)
        controls.update_inos(inos)

run()