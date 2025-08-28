class CharacterLogic:
    def __init__(self, pos):
        self.health = 100
        self.mana = 50
        self._pos = pos
        # other shared logic attributes

    @property
    def pos(self):
        return self._pos

    @pos.setter
    def pos(self, value):
        self._pos = value
        if hasattr(self, "sprite"):
            self.sprite.update_position(value)