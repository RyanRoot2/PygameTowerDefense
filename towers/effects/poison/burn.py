import pygame
from burn.consecration import Consecration

from settings import ACTORS
from towers.base_tower import CharacterLogic
from utils.base_sprite import BaseSprite


class Paladin(CharacterLogic):
    dynamic_layering = True
    layer = ACTORS

    def __init__(self, pos, *groups):
        super().__init__(pos)
        self.holy_power = 0
        self.groups = groups
        self.sprite = BaseSprite(
            self.pos, "assets/paladin.png", type(self).dynamic_layering, type(self).layer, *self.groups
        )
        # unique paladin logic

    def cast_consecration(self):
        consecration = Consecration(self.pos, *self.groups)  # noqa: F841

    def use_abilities(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_1]:
            self.cast_consecration()
        # other ability checks
