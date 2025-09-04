from pathlib import Path

import pygame

from tower_defense.settings import ACTORS
from tower_defense.towers.base_tower import CharacterLogic
from tower_defense.towers.effects.burn.consecration import Consecration
from tower_defense.utils.base_sprite import BaseSprite


class Paladin(CharacterLogic):
    dynamic_layering = True
    layer = ACTORS

    def __init__(self, pos, *groups):
        super().__init__(pos)
        self.holy_power = 0
        self.groups = groups
        self.sprite = BaseSprite(
            self.pos, Path("assets/paladin.png"), type(self).dynamic_layering, type(self).layer, *self.groups
        )
        # unique paladin logic

    def cast_consecration(self):
        consecration = Consecration(self.pos, *self.groups)  # noqa: F841

    def use_abilities(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_1]:
            self.cast_consecration()
        # other ability checks
