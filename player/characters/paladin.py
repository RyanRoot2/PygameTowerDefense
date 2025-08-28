from utils.base_sprite import BaseSprite
from player.character_logic import CharacterLogic

class Paladin(CharacterLogic):
    def __init__(self, pos):
        super().__init__(pos)
        self.holy_power = 0
        self.sprite = BaseSprite(self.pos, "assets/paladin.png")
        # unique paladin logic