import inspect, player.character_sprite
print(inspect.getmembers(player.character_sprite))

import pygame
import sys
from player.characters.paladin import Paladin

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Simple Pygame Window")


class Player(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.image.load("assets/paladin.png").convert()
        self.rect = self.image.get_rect(topleft=pos)

player = Player((100, 100))
all_sprites = pygame.sprite.Group(player)


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
    all_sprites.draw(screen)
    player2_group.draw(screen)
    


      # Fill the screen with black
    pygame.display.flip()  # Update the display