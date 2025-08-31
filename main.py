from settings import *
import pygame
import sys
from player.characters.paladin import Paladin
from ui_elements.healthbar import HealthBar

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Simple Pygame Window")



testing_group = pygame.sprite.Group()
player2 = Paladin((0, 0), testing_group)
player2.pos = (200, 200)
player2.sprite.update_position(player2.pos)
player2_group = pygame.sprite.Group(player2.sprite)
healthbar = HealthBar(width=200, height=20, color=(0, 255, 0), attached_object=None, border=True, pos=(50, 50))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((100, 100, 100))  # Fill the screen with black
    player2.update()
    player2.use_abilities()
    player2_group.draw(screen)
    testing_group.draw(screen)
    healthbar.draw(screen, player2.health, player2.max_health)  # Example health values
    
    # Fill the screen with black
    pygame.display.flip()  # Update the display