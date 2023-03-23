import pygame, sys
from bullet import Bullet
from inc import Ino
def events(screen, hi, bullets):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:

            if event.key == pygame.K_d:
                hi.mright = True
            elif event.key == pygame.K_a:
                hi.mleft = True
            elif event.key == pygame.K_SPACE:
                new_bullet = Bullet(screen , hi)
                bullets.add(new_bullet)
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_d:
                hi.mright = False
            elif event.key == pygame.K_a:
                hi.mleft = False

def update(bg_color, screen, hi,inos,  bullets):

    for bullet in bullets.sprites():
        bullet.draw_bullet()

    hi.output()
    inos.draw(screen)
    pygame.display.flip()
def update_bullets(inos, bullets) :
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    collisions = pygame.sprite.groupcollide(bullets, inos , True, True)


def update_inos(inos):
    inos.update()

def create_army(screen, inos):
    inc = Ino(screen)
    inc_wight = inc.rect.width
    numbers_inc_x = int((800 - 6 * inc_wight) / inc_wight)
    inc_hight = inc.rect.height
    numbers_inc_y = int((1000 - 200 - 2 * inc_hight) / inc_hight)

    for row_number in range(numbers_inc_y - 1):

        for inc_number in range(numbers_inc_x):
            inc = Ino(screen)
            inc.x = inc_wight + inc_wight * inc_number
            inc.y = inc_hight + inc_hight * row_number
            inc.rect.x = inc.x
            inc.rect.y = inc.rect.height + 2 * inc.rect.height * row_number
            inos.add(inc)
