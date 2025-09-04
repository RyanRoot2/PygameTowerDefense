from settings import EFFECTS
from utils.base_sprite import BaseSprite


class Consecration:
    dynamic_layering = True
    layer = EFFECTS

    def __init__(self, pos, *groups):
        self.name = "Consecration"
        self.pos = pos
        self.sprite = BaseSprite(
            self.pos, "assets/consecration.png", type(self).dynamic_layering, type(self).layer, *groups
        )

        print(f"{self.name} cast at position {pos}")
