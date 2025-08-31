from utils.base_sprite import BaseSprite
from player.character_logic import CharacterLogic
from abilities.consecration import Consecration
import pygame

class Paladin(CharacterLogic):
    def __init__(self, pos, *groups):
        super().__init__(pos)
        self.holy_power = 0
        self.sprite = BaseSprite(self.pos, "assets/paladin.png")
        # unique paladin logic
        self.groups = groups

    def cast_consecration(self):
        consecration = Consecration(self.pos, *self.groups)

    def use_abilities(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_1]:
            self.cast_consecration()
        # other ability checks