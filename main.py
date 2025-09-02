from settings import *
import pygame
import sys
from towers.effects.burn.burn import *

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Simple Pygame Window")

groups = {
    'background': pygame.sprite.Group(),
    'terrain': pygame.sprite.Group(),
    'effects': pygame.sprite.Group(),
    'actors': pygame.sprite.Group(),
    'projectiles': pygame.sprite.Group(),
    'ui': pygame.sprite.Group(),
}
all_sprites = pygame.sprite.LayeredUpdates()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((100, 100, 100))  # Fill the screen with black
    all_sprites.draw(screen)
    
    # Fill the screen with black
    pygame.display.flip()  # Update the display