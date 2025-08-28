from settings import *
import pygame
import sys
from player.characters.paladin import Paladin

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Simple Pygame Window")


player2 = Paladin((0, 0))
player2.pos = (200, 200)
player2.sprite.update_position(player2.pos)
player2_group = pygame.sprite.Group(player2.sprite)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((0, 0, 0))  # Fill the screen with black
    player2.update()
    player2_group.draw(screen)
    
    # Fill the screen with black
    pygame.display.flip()  # Update the display