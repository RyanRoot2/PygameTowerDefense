import sys
from typing import NamedTuple

import pygame

from tower_defense.settings import SCREEN_HEIGHT, SCREEN_WIDTH


class SpriteGroups(NamedTuple):
    background: pygame.sprite.Group = pygame.sprite.Group()
    terrain: pygame.sprite.Group = pygame.sprite.Group()
    effects: pygame.sprite.Group = pygame.sprite.Group()
    actors: pygame.sprite.Group = pygame.sprite.Group()
    projectiles: pygame.sprite.Group = pygame.sprite.Group()
    ui: pygame.sprite.Group = pygame.sprite.Group()


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Simple Pygame Window")

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


if __name__ == "__main__":
    main()
