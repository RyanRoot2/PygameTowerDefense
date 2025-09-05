import random
import sys
from typing import NamedTuple

import pygame
from pygame.math import Vector2

from tower_defense.settings import SCREEN_HEIGHT, SCREEN_WIDTH
from tower_defense.utils.asset_manager import Images
from tower_defense.utils.base_sprite import BaseSprite


class SpriteGroups(NamedTuple):
    background: pygame.sprite.Group = pygame.sprite.Group()
    terrain: pygame.sprite.Group = pygame.sprite.Group()
    effects: pygame.sprite.Group = pygame.sprite.Group()
    actors: pygame.sprite.Group = pygame.sprite.Group()
    projectiles: pygame.sprite.Group = pygame.sprite.Group()
    ui: pygame.sprite.Group = pygame.sprite.Group()


def make_reginald(group: pygame.sprite.Group):
    """Silly test function to add a sprite at a random location."""
    location = Vector2(
        random.randint(0, SCREEN_WIDTH),
        random.randint(0, SCREEN_HEIGHT),
    )
    reginald = BaseSprite(location, Images.ZOMBIE.load())
    group.add(reginald)


def setup() -> tuple[pygame.Surface, SpriteGroups]:
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Tower Defense Game")

    sprite_groups = SpriteGroups()
    # all_sprites = pygame.sprite.LayeredUpdates()

    return screen, sprite_groups


def event_handler(sprite_groups: SpriteGroups):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            match event.key:
                case pygame.K_q, pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                case pygame.K_f:
                    pygame.display.toggle_fullscreen()
                case pygame.K_SPACE:
                    make_reginald(sprite_groups.actors)


def main_loop(screen: pygame.Surface, sprite_groups: SpriteGroups):
    while True:
        event_handler(sprite_groups)

        screen.fill(pygame.Color("grey40"))
        for group in sprite_groups:
            group.draw(screen)
        # all_sprites.draw(screen)

        pygame.display.flip()  # Update the display


def main():
    screen, sprite_groups = setup()
    main_loop(screen, sprite_groups)


if __name__ == "__main__":
    main()
