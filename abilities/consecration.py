from utils.base_sprite import BaseSprite

class Consecration:
    def __init__(self, pos, *groups):
        self.name = "Consecration"
        self.pos = pos
        self.sprite = BaseSprite(self.pos, "assets/consecration.png", *groups)
        
        print(f"{self.name} cast at position {pos}")
