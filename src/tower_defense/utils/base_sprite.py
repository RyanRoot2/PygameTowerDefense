from pathlib import Path

import pygame

from tower_defense.settings import BACKGROUND


class BaseSprite(pygame.sprite.Sprite):
    def __init__(self, pos, image_path: Path, dynamic_layering=False, layer=BACKGROUND, *groups):
        super().__init__(*groups)
        self.image = pygame.image.load(image_path).convert_alpha()
        self.rect: pygame.Rect = self.image.get_rect(topleft=pos)
        self.dynamic_layering = dynamic_layering
        self.layer = layer

    def update_position(self, new_pos):
        self.rect.topleft = new_pos
