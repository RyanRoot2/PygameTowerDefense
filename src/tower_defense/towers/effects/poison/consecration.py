from pathlib import Path

from tower_defense.settings import EFFECTS
from tower_defense.utils.base_sprite import BaseSprite


class Consecration:
    dynamic_layering = True
    layer = EFFECTS

    def __init__(self, pos, *groups):
        self.name = "Consecration"
        self.pos = pos
        self.sprite = BaseSprite(
            self.pos, Path("assets/consecration.png"), type(self).dynamic_layering, type(self).layer, *groups
        )

        print(f"{self.name} cast at position {pos}")
